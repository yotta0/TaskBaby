# Third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local application imports
from .serializers import TaskListSerializer


class TaskListCreateView(APIView):

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
                    'data': None
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
