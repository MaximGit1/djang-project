from book_storage.models import Genre, TypeOfBook

menu = (('Авторы', 'authors_page'), ('О нас', 'about'))
genres_all = Genre.objects.all()
types_all = TypeOfBook.objects.all()
DATA = {'genres_all': genres_all, 'types_all': types_all, 'menu': menu}