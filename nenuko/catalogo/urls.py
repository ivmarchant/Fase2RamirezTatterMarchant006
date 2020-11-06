from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mangas/', views.mangas, name='mangas'),
    path('figuras/', views.figuras, name='figuras'),
    path('registro/', views.registro, name='registro'),
    path('mangaka/<int:pk>', views.MangakaDetailView.as_view(), name='mangaka-detail'),
]
urlpatterns +=[
    path('mangaka/create/', views.MangakaCreate.as_view(), name='mangaka_create'),
    path('mangaka/<int:pk>/update/', views.MangakaUpdate.as_view(), name='mangaka_update'),
    path('mangaka/<int:pk>/delete/', views.MangakaDelete.as_view(), name='mangaka_delete'),
]