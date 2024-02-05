from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    id_autor = models.IntegerField()
    writing_year = models.IntegerField()  #чекнуть max len
    id_publisher = models.IntegerField()
    id_genre = models.IntegerField()
    description = models.TextField()
    book_image = models.ImageField(upload_to="book-photos/%Y")
    fb2_path = models.FilePathField()
    epub_path = models.FilePathField()
    mp3_path = models.FilePathField()
    book_feedback = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
