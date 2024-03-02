from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import *


menu = (('Жанры', 'home'), ('Авторы', 'authors_page'), ('Издательство', 'home'), ('О нас', 'home'))  # 'Онлайн библиотека',

class LibraryHome(ListView):
    model = Book
    template_name = 'book_storage/index.html'
    context_object_name = 'books'
    extra_context = {'title': 'Главная', 'menu': menu}
    #paginate_by = 12


def book_page(request, id_book):
    book = Book.objects.get(pk=id_book)
    book_ser = bool(book.book_series)
    ser_books = Book.objects.filter(book_series=book_ser) if book_ser else False
    if ser_books:
        ser_books = [(b.book_ind, b.title, b.pk) for b in ser_books]
        ser_books.sort()

    genres = book.id_genre.all()
    author = book.id_author
    data = {'title': f'Книга {book.title}', 'book': book, 'genres': genres, 'menu': menu, 'author': author, 'ser_books': ser_books}
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