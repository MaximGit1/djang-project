from django.contrib import admin
from . import models
from django.contrib.admin import register

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_update', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('time_update', 'time_create')

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('publisher_name',)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('fio_author',)


admin.site.register(models.Genre)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.TypeOfBook)
admin.site.register(models.BookSeries)
admin.site.register(models.LikedBook)  ## del