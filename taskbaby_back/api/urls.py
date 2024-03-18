from django.urls import path, include

urlpatterns = [
    path('tasks/', include('task_app.urls')),
]
