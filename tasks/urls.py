from django.urls import path
from .views import list_task, create_task

urlpatterns = [
    path("", list_task),
    path("new_task/", create_task, name="create_task"),
]
