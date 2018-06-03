from django.conf.urls import url

from . import views

app_name = 'resturant'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='listView'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detailView'),
    url(r'^makeentry$', views.makeentry, name='makeentry'),
]