from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.home, name="home"),
    path("wiki/<str:title>", views.detail, name="detail"),
    path("search/", views.search, name="search"),
    path("random-page/", views.rand, name="random"),
    path("create/", views.create, name="create"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),

]