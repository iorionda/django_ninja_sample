from django.urls import path

from api.api_v1 import app

urlpatterns = [
    path("v1/", app.urls, name="api-v1"),
]
