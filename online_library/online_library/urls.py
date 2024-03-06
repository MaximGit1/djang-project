from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from book_storage.views import index
from online_library import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_storage.urls')),
    path('users/', include('users.urls', namespace='users')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)