from django.shortcuts import render
from django.views import generic

from .forms import CollegeForm
from .models import College
# Create your views here.
# normal view to handle the entry of the product and store it on the database
def makeentry(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)

        if form.is_valid():
            cid = request.POST.get('cid', '')
            name = request.POST.get('name', '')
            area = request.POST.get('area', '')
            ratings = request.POST.get('ratings', '')
            field = request.POST.get('field', '')

        product = College(cid=cid,
                          name=name, area=area, ratings=ratings, field=field)
        product.save()

        form = CollegeForm()

        return render(request, 'College/makeentry.html', {'form': form})
    else:
        form = CollegeForm()
        return render(request, 'College/makeentry.html', {'form': form})


# generic view to fetch the data then show in a list
class IndexView(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'College_list'
    template_name = 'College/index.html'

    def get_queryset(self):
        return College.objects.all()


# generic view to show the details of a particular object
class DetailsView(generic.DetailView):
    model = College
    template_name = 'College/detail.html'
