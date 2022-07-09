from tempfile import template
from django.urls import path

from . import views,execute

urlpatterns = [
    path('', views.index, name='index'),
    path('problems', views.problem, name='problem'),
    path('problems/<int:problemId>/', views.detail, name='detail'),
    path('problems/submit/<int:problemId>/', execute.submit, name='submit'),
    path('submissions', views.submission, name='submission'),
    path('customtest', views.customtest, name='customtest'),
]
