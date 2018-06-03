from django.shortcuts import render
from django.views import generic

from .forms import EmployeForm
from .models import Employe
# Create your views here.
# normal view to handle the entry of the product and store it on the database
def makeentry(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)

        if form.is_valid():
            title = request.POST.get('title', '')
            title1 = request.POST.get('title1', '')
            title2 = request.POST.get('title2', '')
            title3 = request.POST.get('title3', '')
            title4 = request.POST.get('title4', '')
            title5 = request.POST.get('title5', '')

        product = Employe(title=title, title1=title1, title2=title2, title3=title3, title4=title4, title5=title5)
        product.save()

        form = EmployeForm()

        return render(request, 'employe/makeentry.html', {'form': form})
    else:
        form = EmployeForm()
        return render(request, 'employe/makeentry.html', {'form': form})


# generic view to fetch the data then show in a list
class IndexView(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'employe_list'
    template_name = 'employe/index.html'

    def get_queryset(self):
        return Employe.objects.all()


# generic view to show the details of a particular object
class DetailsView(generic.DetailView):
    model = Employe
    template_name = 'employe/detail.html'
