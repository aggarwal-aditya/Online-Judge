from django.urls import path

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('login/', views.login, name="login"),
    path('login/', views.login_page, name='login'),
    path('signin/', views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path('register/', views.register, name='register'),
]
