from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm, RegisterUserForm, UserNickForm
from book_storage.models import LikedBook, Book

menu = (('Жанры', 'home'), ('Авторы', 'authors_page'), ('Издательство', 'home'), ('О нас', 'home'))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

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
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    #form = UserNickForm()  'form': form
    user_id = request.user.id #  filter(user=user_id)
    lk_books = LikedBook.objects.filter(user=user_id)

    context = {'title': 'Личный кабинет', 'menu': menu, 'user': request.user, 'lk_books': lk_books}
    return render(request, 'users/profile.html', context)