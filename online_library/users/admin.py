from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'nickname', 'avatar', 'is_active')
    readonly_fields = ('username',)
    list_display = ('username', 'nickname')
    search_fields = ('username', 'nickname')
