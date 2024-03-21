# Third party imports
from rest_framework import serializers

# Local application imports
from .models import TaskList, TaskItem


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)

    def validate(self, data):
        if TaskList.objects.filter(title=data['title']).exists():
            raise serializers.ValidationError('Task List with this title already exists')
        return data

    def create(self, validated_data):
        task_list = TaskList.objects.create(
            title=validated_data['title']
        )
        task_list.save()
        return task_list


class TaskItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField()
    completed = serializers.BooleanField()

    def create(self, validated_data):
        task_item = TaskItem.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            due_date=validated_data['due_date'],
            completed=validated_data['completed'],
            task_list=validated_data['task_list']
        )
        task_item.save()
        return task_item
