from django.contrib import admin
from . import models
from django.contrib.admin import register

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title',)



admin.site.register(models.Genre)
admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.TypeOfBook)