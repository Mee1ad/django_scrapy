from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search_movie/$', views.search_movie, name='search_movie'),
    url(r'^get_movie/$', views.get_movie, name='get_movie'),
    url(r'^search_serial/$', views.search_movie, name='search_movie'),
    url(r'^get_serial/$', views.get_movie, name='get_movie'),
]
