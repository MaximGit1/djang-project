from django.contrib import admin
from . import models
from django.contrib.admin import register


admin.site.register(models.Genre)
admin.site.register(models.Autor)
admin.site.register(models.Publisher)
admin.site.register(models.Book)