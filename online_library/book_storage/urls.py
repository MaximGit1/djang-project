from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('genre/<int:id_genre>', home, name='home_genre'),
    path('type/<int:type_of_book>', home, name='home_type'),
    path('book/<int:id_book>/', book_page, name='book_page'),
    path('book/add/<int:id_book>/', add_liked_book, name='book_add'),
    path('book/remove/<int:id_lk_book>/', remove_liked_book, name='book_remove'),
    path('book-read/<int:id_book>/', read_page, name='read_page'),
    path('author/<int:id_author>/', author_page, name='author_page'),
    path('authors/', authors_page, name='authors_page'),
    path('about/', about_page, name='about'),
    path('book/<int:id_book>/rating/<int:value>/', add_book_rating, name='book_rating_change'),
    path('book/<int:id_book>/comment/', book_comments, name='book_comment'),
    path('book/comment/<int:id_comment>', delete_comment, name='delete_comment'),
    path('search/', search, name='search'),
    path('tags/', tags_page, name='tags_page'),
    path('generate/<path:book_search>/', generate, name='generate'),
    path('generate-create/<path:book_url>/', create_generated_book, name='generate_create'),
]