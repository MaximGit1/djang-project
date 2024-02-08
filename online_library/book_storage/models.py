import string, random as rnd

from django.db import models

class Author(models.Model):
    fio_author = models.CharField(max_length=50)

    def __str__(self):
        return self.fio_author

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.publisher_name

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre



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
    title = models.CharField(max_length=50)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    writing_year = models.IntegerField()
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    book_image = models.ImageField(upload_to=f"books/%Y/%m{file_path}")
    fb2_path = models.FileField(upload_to=f"books/%Y/%m{file_path}")
    epub_path = models.FileField(upload_to=f"books/%Y/%m{file_path}")  #blank
    mp3_path = models.FileField(upload_to=f"books/%Y/%m{file_path}")  #blank
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



