from django.conf.urls import url

from . import views

app_name = 'employe'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    url(r'^makeentry$', views.makeentry, name='makeentry'),
]