from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm, RegisterUserForm, UserEditForm
from book_storage.models import LikedBook, Book
from .models import User

menu = (('Жанры', 'home'), ('Авторы', 'authors_page'), ('Издательство', 'home'), ('О нас', 'about'))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация', 'menu': menu}

    def get_success_url(self):
        return reverse_lazy('home')

def logout_users(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def register_users(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form, 'menu': menu})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if len(str(form.data.get('nickname')).replace(' ', '')) >= 3:
                form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserEditForm(instance=request.user)
    user_id = request.user.id
    lk_books = LikedBook.objects.filter(user=user_id)
    context = {'title': 'Личный кабинет', 'menu': menu, 'user': request.user, 'lk_books': lk_books, 'form': form}
    return render(request, 'users/profile.html', context)

def other_profile(request, id_user):
    user_sel = User.objects.get(pk=id_user)
    if request.user.is_authenticated:
        if request.user.username == user_sel.username:
            return HttpResponseRedirect(reverse('users:profile'))
    lk_books = LikedBook.objects.filter(user=id_user)
    context = {'title': 'Профиль', 'menu': menu, 'user': user_sel, 'lk_books': lk_books}
    return render(request, 'users/other-profile.html', context)