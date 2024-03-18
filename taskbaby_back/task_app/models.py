from django.db import models


class TaskList(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class TaskItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.task_list}'
