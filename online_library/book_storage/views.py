from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения")

def book_page(request, id_book):
    return HttpResponse(f"book has {id_book} id")