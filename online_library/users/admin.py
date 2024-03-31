from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('user_nick', 'avatar_photo', 'nickname', 'avatar', 'is_active')
    readonly_fields = ('username', 'avatar_photo', 'user_nick')
    list_display = ('user_nick', 'avatar_photo', 'nickname')
    search_fields = ('username', 'nickname')
    list_display_links = ('user_nick', 'avatar_photo', 'nickname')

    @admin.display(description='Аватар')
    def avatar_photo(self, user):
        if user.avatar:
            return mark_safe(f"<img src='{user.avatar.url}' width=70px>")
        return 'Без фото'

    @admin.display(description='Уникальное имя')
    def user_nick(self, user):
        color = 'red' if user.is_superuser else 'white'
        return mark_safe(f'<h3 style="color:{color}">@{user.username}</h3>')
