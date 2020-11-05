from django.shortcuts import render
from . models import Manga, MangaInstance,Mangaka,Genre
from django.views import generic
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

class MangaListView(generic.ListView):
    model = Manga
    paginate_by = 10
class MangaDetailView(generic.DetailView):
    model = Manga