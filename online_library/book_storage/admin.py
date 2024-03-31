from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
from django.contrib.admin import register


class BookAdmin(admin.ModelAdmin):
    fields = (
    'title', 'book_photo', 'book_image', 'id_author', 'book_series', 'book_ind', 'writing_year', 'id_publisher',
    'id_genre', 'type_of_book', 'description', 'read_text', 'fb2_path', 'epub_path', 'mp3_path', 'is_published', 'is_verified')
    list_display = ('title', 'book_photo', 'time_update', 'time_create', 'is_published', 'is_verified')
    list_display_links = ('title', 'book_photo')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('time_update', 'time_create')
    filter_horizontal = ('id_genre',)
    readonly_fields = ('book_photo',)
    save_on_top = True
    actions = ('set_published', 'set_verified')

    @admin.display(description='Обложка книги')
    def book_photo(self, book):
        if book.book_image:
            return mark_safe(f"<img src='{book.book_image.url}' width=70px>")
        return 'Без фото'

    @admin.action(description='Поменять статус публикации')
    def set_published(self, request, queryset):
        for book in queryset:
            book.is_published = not bool(book.is_published)
            book.save()
        self.message_user(request, f'Изменено {len(queryset)} записей')

    @admin.action(description='Поменять статус верефикации')
    def set_verified(self, request, queryset):
        for book in queryset:
            book.is_verified = not bool(book.is_verified)
            book.save()
        self.message_user(request, f'Изменено {len(queryset)} записей')


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('publisher_name',)


class AuthorAdmin(admin.ModelAdmin):
    fields = ('fio_author', 'author_photo', 'photo', 'biography')
    readonly_fields = ('author_photo',)
    search_fields = ('fio_author',)
    list_display = ('fio_author', 'author_photo')

    @admin.display(description='Автор')
    def author_photo(self, author):
        if author.photo:
            return mark_safe(f"<img src='{author.photo.url}' width=70px>")
        return 'Без фото'



@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('genre',)

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.TypeOfBook)
admin.site.register(models.BookSeries)
