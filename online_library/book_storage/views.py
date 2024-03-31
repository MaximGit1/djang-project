from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .forms import CommentForm
from .models import *
from django.views.decorators.http import require_POST
from django.db.models import Q
from global_values import DATA
import parse
import asyncio

def home(request, id_genre=None, type_of_book=None):
    if id_genre:
        books = Book.objects.filter(id_genre=id_genre, is_published=True)
        message = f'Все книги с жанром: {Genre.objects.get(pk=id_genre)}'
    elif type_of_book:
        books = Book.objects.filter(type_of_book=type_of_book, is_published=True)
        message = f'Все книги с тегом: {TypeOfBook.objects.get(pk=type_of_book)}'
    else:
        books = Book.objects.filter(is_published=True)
        message = ''
    genres = Genre.objects.all()
    types = TypeOfBook.objects.all()
    paginator = Paginator(books, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {**DATA, 'title': 'Главная', 'books': books, 'message': message, 'page_obj': page_obj}
    return render(request, 'book_storage/index.html', context)


def book_page(request, id_book):
    book = Book.objects.get(pk=id_book)  # выбор книги по id
    ser_books = False
    if book.book_series:
        ser = book.book_series
        ser_bks = Book.objects.filter(book_series=ser)
        ser_books = []
        for b in ser_bks:
            ser_books.append(
                [b.book_ind,
                {'title': b.title, 'pk': b.pk}
                 ])
        try:
            ser_books.sort()
        except:
            pass
        ss = [sb[-1] for sb in ser_books]
        ser_books = ss
    genres = book.id_genre.all()
    author = book.id_author
    rate = 0
    if request.user.is_authenticated:
        rate = BookRating.objects.filter(user=request.user, book=book)
        if rate.exists():
            rate = BookRating.objects.get(user=request.user, book=book)
            rate = rate.rating
    comments = Comment.objects.filter(book=id_book, active=True)
    form = CommentForm  # ()
    check = False
    if request.user.is_authenticated:
        user = request.user
        check_comment = Comment.objects.filter(book=id_book, user=user)
        check = not bool(check_comment)

    data = {**DATA, 'title': f'Книга {book.title}', 'book': book, 'genres': genres, 'author': author,
            'ser_books': ser_books, 'rate': rate, 'comments': comments, 'form': form, 'check': check}
    return render(request, 'book_storage/book_page.html', data)


def author_page(request, id_author):
    author = Author.objects.get(pk=id_author)
    all_books = Book.objects.filter(id_author=id_author)
    serias_books, books = set(), []
    for b in all_books:
        if b.book_series != None:
            serias_books.add(b.book_series)
        else:
            books.append(b)
    books_in_seria = []
    for b in serias_books:
        try:
            seria = BookSeries.objects.get(book_series=b.book_series)
            books_in_seria.append(Book.objects.filter(book_series=seria))
        except:
            pass
    data = {**DATA, 'title': f'Страница автора', 'author': author, 'books': books, 'books_in_seria': books_in_seria}
    return render(request, 'book_storage/author_page.html', data)


def authors_page(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    data = {**DATA, 'title': f'Все авторы', 'authors': authors}
    return render(request, 'book_storage/authors_page.html', data)


@login_required
def add_liked_book(request, id_book):
    book = Book.objects.get(pk=id_book)
    lk_book = LikedBook.objects.filter(user=request.user, liked_book=book)
    if not lk_book.exists():
        LikedBook.objects.create(user=request.user, liked_book=book)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_liked_book(request, id_lk_book):
    lk_book = LikedBook.objects.get(pk=id_lk_book)
    lk_book.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def read_page(request, id_book):
    book = Book.objects.get(pk=id_book)
    data = {**DATA, 'title': f'{book.title}', 'book': book}
    return render(request, 'book_storage/read_page.html', data)


def about_page(request):
    context = {**DATA, 'title': 'Кто мы?'}
    return render(request, 'book_storage/about.html', context)


@login_required
def add_book_rating(request, id_book, value):
    if value == 1:
        value = 1
    elif value == 2:
        value = -1
    else:
        value = 0
    book = Book.objects.get(pk=id_book)
    book_rating = BookRating.objects.filter(user=request.user, book=book)
    if not book_rating.exists():
        BookRating.objects.create(user=request.user, book=book, rating=value)
        book.rating += value
        book.save()
    else:
        book_rating = BookRating.objects.get(book=book, user=request.user)
        if book_rating.rating != value:
            book_rating.rating = value
            book_rating.save()
            book.rating += (value * 2)
            book.save()
    uri = reverse('book_page', args=(id_book,))
    return redirect(uri)


def book_comments(request, id_book):   # try to del
    book1 = Book.objects.get(pk=id_book)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            text = form.data.get('text')
            Comment.objects.create(user=request.user, book=book1, text=text)
            uri = reverse('book_page', args=(id_book,))
            return redirect(uri)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'book_storage/comment.html', context)


@login_required
def delete_comment(request, id_comment):
    comment = Comment.objects.get(pk=id_comment)
    id_book = comment.book.id
    uri = reverse('book_page', args=(id_book,))
    if request.user == comment.user:
        comment.delete()
    return redirect(uri)


def search(request):
    search_quary = request.GET.get('search-all', '')
    if search_quary:
        books = Book.objects.filter(Q(title__icontains=search_quary) | Q(description__icontains=search_quary),
                                    is_published=True)
        authors = Author.objects.filter(fio_author__icontains=search_quary)
        # seria = BookSeries.objects.filter(book_series__icontains=search_quary)
    else:
        return HttpResponseRedirect(reverse('home'))

    data = {**DATA, 'title': 'Результаты поиска', 'books': books, 'authors': authors, 'search_quary_': search_quary}
    return render(request, 'book_storage/search_page.html', data)


def tags_page(request):  # try to del
    genres = Genre.objects.all()
    types = TypeOfBook.objects.all()
    data = {'title': 'Выбрать книгу', 'genres': genres, 'types': types, }
    return render(request, 'book_storage/tags_page.html', data)

def generate(request, book_search):
    search_quary = book_search
    if search_quary:
        loop = asyncio.new_event_loop()
        res = loop.run_until_complete(parse.main(search_quary))
        #return HttpResponse('res:', res)
        data = {**DATA, 'resources': res}
        return render(request, 'book_storage/generate_page.html', data)


def create_generated_book(request, book_url):
    loop = asyncio.new_event_loop()
    res = loop.run_until_complete(parse.download_book(book_url))
    if Author.objects.filter(fio_author=res['author']).exists():
        current_author = Author.objects.get(fio_author=res['author'])
    else:
        res_author = loop.run_until_complete(parse.author_parse(res['author_url']))
        current_author = Author.objects.create(fio_author=res_author['author_fio'], biography=res_author['bio'], photo=res_author['img'])
    if res['seria']:
        if BookSeries.objects.filter(book_series=res['seria']).exists():
            current_seria = BookSeries.objects.get(book_series=res['seria'])
        else:
            current_seria = BookSeries.objects.create(book_series=res['seria'])
    else:
        current_seria = None


    book = Book.objects.create(title=res['title'], id_author=current_author, book_series=current_seria, writing_year=res['year'],
                               id_publisher=Publisher.objects.get(pk=1),
                               type_of_book=TypeOfBook.objects.get(pk=4), description=res['description'], read_text='Не сгенерировано',
                               book_image=res['img'], fb2_path=res['fb2'], epub_path=res['epub'])
    for tag in res['tags']:
        if not Genre.objects.filter(genre=tag).exists():
            current_tag = Genre.objects.create(genre=tag)
        else:
            current_tag = Genre.objects.get(genre=tag)
        book.id_genre.add(current_tag)
    uri = reverse('book_page', args=(book.pk,))
    return redirect(uri)


    #return HttpResponse(f'text: {book_url}\nAuthor --> exists\nres = {res}')