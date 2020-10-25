# from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from search import views
from . import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^search/$', views.searching, name='search'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^mentions/$', views.mentions),
]