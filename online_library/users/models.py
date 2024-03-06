from django.contrib.auth.models import AbstractUser
from django.db import models
from random import randint as rn



class User(AbstractUser):
    class GenerateName:
        @classmethod
        def set_name(cls):
            nick = 'user' + ''.join([str(rn(0, 9)) for n in range(10)])
            return nick
    #nick = 'user-%t'
    nick = GenerateName.set_name()
    avatar = models.ImageField(upload_to='users/%Y/%m', blank=True, null=True, verbose_name='Аватар')
    nickname = models.CharField(default=nick, max_length=15, verbose_name='Отображаемое имя')
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


