from django.contrib import admin

# Register your models here.
from . models import Genre, Manga, Mangaka, MangaInstance

admin.site.register(Manga)
admin.site.register(Mangaka)
admin.site.register(Genre)
admin.site.register(MangaInstance)