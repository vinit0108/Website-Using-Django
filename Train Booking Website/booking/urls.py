from django.conf.urls import url

from . import views

app_name = 'bookviews'

urlpatterns = [

    url(r'^$', views.makeentry, name='makeentry'),
    url(r'^v$', views.IndexView.as_view(), name='index'),
    url(r'^search$', views.Search, name='search')
]
