from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import *


menu = (('Жанры', 'home'), ('Авторы', 'authors_page'), ('Издательство', 'home'), ('О нас', 'about'))

#class LibraryHome(ListView):
#    model = Book
#    template_name = 'book_storage/index.html'
#    context_object_name = 'books'
#    extra_context = {'title': 'Главная', 'menu': menu}
#    #paginate_by = 12

def home(request, id_genre=None, type_of_book=None):
    if id_genre:
        books = Book.objects.filter(id_genre=id_genre)
        message = f'Все книги с жанром: {Genre.objects.get(pk=id_genre)}'
    elif type_of_book:
        books = Book.objects.filter(type_of_book=type_of_book)
        message = f'Все книги с тегом: {TypeOfBook.objects.get(pk=type_of_book)}'
    else:
        books = Book.objects.all()
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
    data = {'title': f'Книга {book.title}', 'book': book, 'genres': genres, 'menu': menu, 'author': author, 'ser_books': ser_books, 'rate': rate}
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