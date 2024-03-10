from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .forms import CommentForm
from .models import *
from django.views.decorators.http import require_POST
from django.db.models import Q

menu = (('Жанры', 'tags_page'), ('Авторы', 'authors_page'), ('О нас', 'about'))


# class LibraryHome(ListView):
#    model = Book
#    template_name = 'book_storage/index.html'
#    context_object_name = 'books'
#    extra_context = {'title': 'Главная', 'menu': menu}
#    #paginate_by = 12

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
    context = {'title': 'Главная', 'menu': menu, 'books': books, 'message': message}
    return render(request, 'book_storage/index.html', context)


def book_page(request, id_book):
    book = Book.objects.get(pk=id_book)
    book_ser = bool(book.book_series)
    ser_books = Book.objects.filter(book_series=book_ser) if book_ser else False
    if ser_books:
        ser_books = [(b.book_ind, b.title, b.pk) for b in ser_books]
        ser_books.sort()

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

    data = {'title': f'Книга {book.title}', 'book': book, 'genres': genres, 'menu': menu, 'author': author,
            'ser_books': ser_books, 'rate': rate, 'comments': comments, 'form': form, 'check': check}
    return render(request, 'book_storage/book_page.html', data)


def author_page(request, id_author):
    author = Author.objects.get(pk=id_author)
    books = Book.objects.filter(id_author=id_author)
    data = {'title': f'Страница автора', 'author': author, 'books': books, 'menu': menu}
    return render(request, 'book_storage/author_page.html', data)


def authors_page(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    data = {'title': f'Все авторы', 'authors': authors, 'menu': menu}
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
    data = {'title': f'{book.title}', 'menu': menu, 'book': book}
    return render(request, 'book_storage/read_page.html', data)


def about_page(request):
    context = {'title': 'Кто мы?', 'menu': menu}
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


def book_comments(request, id_book):
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
        #seria = BookSeries.objects.filter(book_series__icontains=search_quary)
    else:
        return HttpResponseRedirect(reverse('home'))

    data = {'title': 'Результаты поиска', 'books': books, 'authors': authors, 'menu': menu}
    return render(request, 'book_storage/search_page.html', data)


def tags_page(request):
    genres = Genre.objects.all()
    types = TypeOfBook.objects.all()
    data = {'title': 'Выбрать книгу', 'genres': genres, 'types': types, 'menu': menu}
    return render(request, 'book_storage/tags_page.html', data)