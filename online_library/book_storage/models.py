import string, random as rnd

from django.db import models
import string, random as rnd

from django.db import models

class Author(models.Model):
    fio_author = models.CharField(max_length=50)
    biography = models.TextField(max_length=2100)  #makemigration
    photo = models.ImageField(upload_to=f"authors/avatar", blank=True)

    def __str__(self):
        return self.fio_author

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.publisher_name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class TypeOfBook(models.Model):
    type_of_book = models.CharField(max_length=16)

    def __str__(self):
        return self.type_of_book

    class Meta:
        verbose_name = 'Тип книги'
        verbose_name_plural = 'Тип книг'


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
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)  # few authors
    #book_series = models.CharField(max_length=50, blank=True)
    writing_year = models.IntegerField()
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_genre = models.ManyToManyField(Genre)
    type_of_book = models.ForeignKey(TypeOfBook, on_delete=models.CASCADE)
    description = models.TextField(max_length=750)
    book_image = models.ImageField(upload_to=f"books/%Y/%m{file_path}")
    fb2_path = models.FileField(upload_to=f"books/%Y/%m{file_path}")
    epub_path = models.FileField(upload_to=f"books/%Y/%m{file_path}", blank=True)
    mp3_path = models.FileField(upload_to=f"books/%Y/%m{file_path}", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['time_update', 'title']

    def __str__(self):
        return self.title