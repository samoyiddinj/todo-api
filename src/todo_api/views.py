from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer

from .models import Todo


class TodoListApiView(APIView):
    def get(self, request, *args, **kwargs):
        # todos = Todo.objects.filter(user=request.user)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    def get_object(self, todo_id):
        try:
            todo_instance = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            todo_instance = None
        return todo_instance

    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response({"error": "todo  id does not find"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response({"error": "todo  id does not find"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(instance=todo_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response({"error": "todo  id does not find"}, status=status.HTTP_404_NOT_FOUND)
        todo_instance.delete()
        return Response({"message": "todo deleted"}, status=status.HTTP_200_OK)

