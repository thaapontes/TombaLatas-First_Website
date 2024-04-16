from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegistrarUsuarioView

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name="logout")
]