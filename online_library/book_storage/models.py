from django.db import models

class Autor(models.Model):
    fio_autor = models.CharField(max_length=50)

    def __str__(self):
        return self.fio_autor

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.publisher_name

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class Book(models.Model):
    title = models.CharField(max_length=50)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    writing_year = models.IntegerField()
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    book_image = models.ImageField(upload_to="book-photos/%Y")
    fb2_path = models.CharField(max_length=100)
    epub_path = models.CharField(max_length=100)
    mp3_path = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
