from django.shortcuts import render
from . models import Manga, MangaInstance, Mangaka, Genre
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    num_Mangas = Manga.objects.all().count()
    num_Mangas_stock = MangaInstance.objects.filter(status__exact='s').count()

    return render(
        request,
        'index.html',
        context={'num_mangas': num_Mangas, 'num_mangas_stock': num_Mangas_stock},
    )
def mangas(request):

    return render(
        request,
        'mangas.html',
       
    )
def figuras(request):
    return render(
        request,
        'figuras.html',
    )
def registro(request):
    return render(
        request,
        'registro.html'
    )
class MangakaCreate(CreateView):
    model = Mangaka
    fields = '__all__'

class MangakaUpdate(UpdateView):
    model = Mangaka
    fields = ['primer_nombre', 'apellido', 'fecha_nacimiento', 'fecha_muerte']

class MangakaDelete(DeleteView):
    model = Mangaka
    success_url = reverse_lazy('index')

class MangakaDetailView(generic.DetailView):
    model=Mangaka

class MangaListView(generic.ListView):
    model = Manga
    paginate_by = 10
class MangaDetailView(generic.DetailView):
    model = Manga