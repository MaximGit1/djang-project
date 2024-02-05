from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('book_page/<int:id_book>/', book_page)
]