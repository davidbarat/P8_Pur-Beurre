# from django.conf.urls import url
from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib import admin
from search import views
from . import views

# app_name = 'search'
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^search/$", views.searching, name="search"),
    url(r"^profile/$", views.profile, name="profile"),
    url(r"^mentions/$", views.mentions, name="mentions"),
    url(r"^search/(?P<barcode>[0-9]+)/$", views.detail, name="detail"),
    url(r"^logout/", views.logout2, name="logout2"),
    # url(r"^login/", views.login2, name="login"),
    url(r"^save/(?P<id>[0-9]+)/", views.save, name="save"),
    url(r"^myproducts/$", views.myproducts, name="myproducts"),
    url(r"^myproducts/(?P<barcode>[0-9]+)/$", views.detail, name="detail"),
]
