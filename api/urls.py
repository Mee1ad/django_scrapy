from django.urls import path,url
from . import views

urlpatterns = [
    url(r'^/api/search_movie/$', views.search_movie, name='search_movie'),
]
