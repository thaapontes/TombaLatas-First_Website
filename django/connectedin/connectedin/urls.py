from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('perfis.urls', 'perfis'), namespace='perfis')),
    path('', include(('users.urls', 'users'), namespace='users'))
]