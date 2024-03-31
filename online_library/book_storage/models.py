import string, random as rnd

from django.db import models
import string, random as rnd

from django.db import models
from users.models import User

class Author(models.Model):
    fio_author = models.CharField(max_length=50, verbose_name='ФИО автора')
    biography = models.TextField(max_length=2100, verbose_name='Биография')
    photo = models.ImageField(upload_to=f"authors/avatar", blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.fio_author

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['fio_author',]


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50, verbose_name='Названия издательства')

    def __str__(self):
        return self.publisher_name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Genre(models.Model):
    genre = models.CharField(max_length=50, verbose_name='Жанр')

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class TypeOfBook(models.Model):
    type_of_book = models.CharField(max_length=50, verbose_name='Тип книги')

    def __str__(self):
        return self.type_of_book

    class Meta:
        verbose_name = 'Тип книги'
        verbose_name_plural = 'Тип книг'


class BookSeries(models.Model):
    book_series = models.CharField(max_length=35, verbose_name='Название цикла')
    class Meta:
        verbose_name = 'Цикл книг'
        verbose_name_plural = 'Циклы книг'

    def __str__(self):
        return self.book_series

class Book(models.Model):
    class Helper:
        @classmethod
        def create_file_path(cls):
            file_path = ''
            for _ in range(6):
                file_path += string.ascii_lowercase[rnd.randint(0, len(string.ascii_lowercase)-1)]
                file_path += str(rnd.randint(0, 9))
            return file_path

    file_path = Helper.create_file_path()
    title = models.CharField(max_length=50, verbose_name='Название')
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')  # few authors
    book_series = models.ForeignKey(BookSeries, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Цикл')
    book_ind = models.SmallIntegerField(verbose_name='Номер в цикле', default=0)
    writing_year = models.IntegerField(verbose_name='Год написания')
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='Издатель')
    id_genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    type_of_book = models.ForeignKey(TypeOfBook, on_delete=models.CASCADE, verbose_name='Тип книги')
    description = models.TextField(max_length=1250, verbose_name='Описание')
    read_text = models.TextField(verbose_name='Содержание книги')
    book_image = models.ImageField(upload_to=f"books/%Y/%m{file_path}", verbose_name='Обложка книги')
    fb2_path = models.FileField(upload_to=f"books/%Y/%m{file_path}", verbose_name='fb2 файл')
    epub_path = models.FileField(upload_to=f"books/%Y/%m{file_path}", blank=True, verbose_name='epub файл')
    mp3_path = models.FileField(upload_to=f"books/%Y/%m{file_path}", blank=True, verbose_name='mp3 файл')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    VERIFIED_STATUS = [(False, 'Не проверено'), (True, 'Проверено')]
    is_verified = models.BooleanField(choices=VERIFIED_STATUS, default=False, verbose_name='Модерация')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-rating', 'time_update', 'title']

    def __str__(self):
        return self.title


class LikedBook(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    liked_book = models.ForeignKey(to=Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'Отложенная книга {self.liked_book.title} для {self.user.username}'

class BookRating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created',]

    def __str__(self):
        return f'Комментарий {self.user} к книге: {self.book}'