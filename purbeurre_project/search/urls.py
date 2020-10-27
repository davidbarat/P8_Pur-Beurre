# from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from search import views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.searching, name='search'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^mentions/$', views.mentions, name='mentions'),
    url(r'^search/(?P<barcode>[0-9]+)/$', views.detail, name='detail'),
]