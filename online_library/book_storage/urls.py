from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('genre/<int:id_genre>', home, name='home'),
    path('type/<int:type_of_book>', home, name='home'),
    path('book/<int:id_book>/', book_page, name='book_page'),
    path('book/add/<int:id_book>/', add_liked_book, name='book_add'),
    path('book/remove/<int:id_lk_book>/', remove_liked_book, name='book_remove'),
    path('book-read/<int:id_book>/', read_page, name='read_page'),
    path('author/<int:id_author>/', author_page, name='author_page'),
    path('authors/', authors_page, name='authors_page'),
    path('about/', about_page, name='about'),
    path('book/<int:id_book>/rating/<int:value>/', add_book_rating, name='book_rating_change'),
]