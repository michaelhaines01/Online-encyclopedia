from django.urls import path

from . import views
# these are the pathways that call functions once activated
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.result, name="title"),
    path("search", views.search, name = "search"),
    path("newpage", views.newpage, name = "newpage"),
    path("editpage", views.editpage, name = "editpage"),
    path("random", views.random, name = "random")
]
