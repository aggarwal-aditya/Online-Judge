from tempfile import template
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('problems', views.problem, name='problem'),
    path('problems/<int:problemId>/', views.detail, name='detail'),
    path('problems/submit/<int:problemId>/', views.submit, name='submit'),
    path('submissions', views.submission, name='submission'),
]
