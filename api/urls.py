from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search_movie/$', views.search_movie, name='search_movie'),
]
