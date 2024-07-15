from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("future", views.future, name="future"),
]
