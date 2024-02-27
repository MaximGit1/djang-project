from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = ('Онлайн библиотека', 'Жанры', 'Авторы', 'Издательство')
def index(request):
    books = Book.objects.all()
    data = {'title': 'Главная страница', 'menu': menu, 'books': books}
    return render(request, 'book_storage/index.html', data)

def book_page(request, id_book):
    book = Book.objects.get(pk=id_book)
    genres = book.id_genre.all()
    data = {'title': f'Книга {book.title}', 'book': book, 'genres': genres, 'menu': menu}
    return render(request, 'book_storage/book_page.html', data)

def author_page(request, id_author):
    author = Author.objects.get(pk=id_author)
    books = Book.objects.filter(id_author=id_author)
    data = {'title': f'Страница автора', 'author': author, 'books': books}
    return render(request, 'book_storage/author_page.html', data)