from django.urls import path

from.views import json_name

urlpatterns = [
    path("", json_name, name="home"),
]