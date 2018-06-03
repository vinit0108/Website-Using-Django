from django.shortcuts import render
from django.views import generic

from .forms import RestForm
from .models import rest
# Create your views here.
# normal view to handle the entry of the product and store it on the database
def makeentry(request):
    if request.method == 'POST':
        form = RestForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            area = request.POST.get('area', '')
            dishes = request.POST.get('dishes', '')
            rating = request.POST.get('rating', '')
        r = rest(name=name, area=area, dishes=dishes , rating=rating)
        r.save()

        form = RestForm()

        return render(request, 'resturant/rest.html', {'form': form})
    else:
        form = RestForm()
        return render(request, 'resturant/rest.html', {'form': form})


# generic view to fetch the data then show in a list
class IndexView(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'rest_list'
    template_name = 'resturant/listView.html'

    def get_queryset(self):
        return rest.objects.all()


# generic view to show the details of a particular object
class DetailsView(generic.DetailView):
    model = rest
    template_name = 'resturant/detialView.html'
