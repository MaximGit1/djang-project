from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = ('Онлайн библиотека', 'Новинки', 'Жанры', 'Авторы', 'Издательство', '[search]')
def index(request):
    books = Book.objects.all()
    data = {'title': 'Главная страница', 'menu': menu, 'books': books}
    return render(request, 'book_storage/index.html', data)

def book_page(request, id_book):
    data = {'title': f'Книга {id_book}', 'id_book': id_book}
    return render(request, 'book_storage/book_page.html', data)

def author_page(request, id_author):
    data = {'title': f'Страница автора', 'id_author': id_author}
    return render(request, 'book_storage/author_page.html', data)