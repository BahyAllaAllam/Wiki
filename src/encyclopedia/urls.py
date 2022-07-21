from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("wiki/<str:title>", views.detail, name="detail"),
    path("search/", views.search, name="search"),
    path("random-page/", views.rand, name="random")
]