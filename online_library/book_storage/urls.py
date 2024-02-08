from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('book/<int:id_book>/', book_page)
]