from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:problemId>/', views.detail, name='detail'),
    # path('<int:problemId>/results/', views.results, name='results'),
]