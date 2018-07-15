from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path(r'^api/search_movie/$', views.search_movie, name='search_movie'),
]
