# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
]