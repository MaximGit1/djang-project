from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'book_storage/index.html', {'title': 'Главная страница'})

def book_page(request, id_book):
    data = {'title': f'Книга {id_book}', 'id_book': id_book}
    return render(request, 'book_storage/book_page.html', data)