from django.urls import path

from .views import TaskListView, TaskItemView

urlpatterns = [
    path('', TaskListView.as_view()),
    path('<int:pk>', TaskItemView.as_view())
]
