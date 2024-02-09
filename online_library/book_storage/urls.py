from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('book/<int:id_book>/', book_page, name='book_page'),
    path('author/<int:id_author>/', author_page, name='author_page'),
]