from tempfile import template
from django.urls import path
from django.views.generic.base import TemplateView

from . import views, execute

urlpatterns = [
    path('', views.index, name='index'),
    path('recent', views.recent, name='recent'),
    path('problems', views.problem, name='problem'),
    path('problems/<int:problemId>/', views.detail, name='detail'),
    path('problems/submit/<int:problemId>/', views.submit, name='submit'),
    path('submissions', views.submission, name='submission'),
    path('customtest', views.customtest, name='customtest'),
]
