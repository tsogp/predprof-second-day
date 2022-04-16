from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index')
] + staticfiles_urlpatterns()