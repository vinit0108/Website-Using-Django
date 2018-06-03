from django.shortcuts import render
from django.views import generic

from .forms import BookingForm
from .forms import Filter
from .models import Booking

# Create your views here.
def makeentry(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            source = request.POST.get('source', '')
            destination = request.POST.get('destination', '')
            date = request.POST.get('date', '')
            time = request.POST.get('time', '')
            adult = request.POST.get('adult', '')
            child = request.POST.get('child', '')
            age = request.POST.get('age', '')

        booking = Booking(source=source, destination=destination,date=date,time=time,adult=adult,child=child,age=age)
        booking.save()

        form = BookingForm()

        return render(request,'bookviews/success.html', {'form': form})
    else:
        form = BookingForm()
        return render(request, 'bookviews/makeentry.html', {'form': form})

class IndexView(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'booking_list'
    template_name = 'bookviews/viewbooking.html'

    def get_queryset(self):
        return Booking.objects.all()

def Search(request):
    if request.method == 'GET':
        form = Filter(request.GET)
        if form.is_valid():
            source = request.GET.get('source', '')
            destination = request.GET.get('destination', '')
            train_list = Booking.objects.filter(source=source,destination=destination)
            context = {
                'form': form,
                'train_list': train_list
            }
        else:
            print('else')
            form = Filter()
            train_list = []
            context = {
                'form': form,
                'train_list': train_list
            }
    else:
        print('else')
        form = Filter()
        train_list =[]
        context = {
            'form': form,
            'train_list': train_list
        }
    return render(request, 'bookviews/Search.html',{'context': context})