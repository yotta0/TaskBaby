# Third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local application imports
from .models import TaskList
from .serializers import TaskListSerializer


class TaskListView(APIView):

    def get(self, request):
        try:
            task_lists = TaskListSerializer(TaskList.objects.all(), many=True)

            return Response(
                {
                    'message': 'Task lists retrieved successfully',
                    'data': task_lists.data
                },
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    'message': 'An error occurred',
                    'data': []
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            data = request.data

            serializer = TaskListSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {
                        'message': 'Invalid data',
                        'data': serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response(
                {
                    'message': 'Task list created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception:
            return Response(
                {
                    'message': 'An error occurred',
                    'data': []
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        try:
            data = request.data

            task_list = TaskList.objects.get(id=data['id'])

            serializer = TaskListSerializer(task_list, data=data)

            if not serializer.is_valid():
                return Response(
                    {
                        'message': 'Invalid data',
                        'data': serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response(
                {
                    'message': 'Task list updated successfully',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    'message': 'An error occurred',
                    'data': []
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        try:
            data = request.data

            task_list = TaskList.objects.get(id=data['id'])

            task_list.delete()

            return Response(
                {
                    'message': 'Task list deleted successfully',
                    'data': []
                },
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    'message': 'An error occurred',
                    'data': []
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
