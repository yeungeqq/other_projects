from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_page", views.create_new_page, name="create_new_page"),
    path("wiki/<str:title>", views.title, name="title"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random")
]
