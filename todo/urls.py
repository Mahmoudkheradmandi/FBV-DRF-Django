from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
   
    path("api/", include("todo.api.urls")),
]