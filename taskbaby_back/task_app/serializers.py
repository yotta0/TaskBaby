# Third party imports
from rest_framework import serializers

# Local application imports
from .models import TaskList


class TaskListSerializer(serializers.Serializer):
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
        return validated_data
