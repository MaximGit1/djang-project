from django.urls import path
from .views import *

app_name = 'users'


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_users, name='logout'),
    path('register/', register_users, name='register'),
    path('profile/', profile, name='profile'),
]