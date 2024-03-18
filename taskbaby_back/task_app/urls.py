from django.urls import path

from .views import TaskListCreateView

urlpatterns = [
    path('create', TaskListCreateView.as_view())
]
