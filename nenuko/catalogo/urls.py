from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mangas/', views.mangas, name='mangas'),
    path('figuras/', views.figuras, name='figuras'),
]