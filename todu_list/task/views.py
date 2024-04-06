from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializer import TaskSerializer,TaskValidateSerializer
from rest_framework import status
# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = TaskValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title=serializer.validated_data['title']
        description=serializer.validated_data['description']
        completed=serializer.validated_data['completed']
        Task.objects.create(title=title, description=description, completed=completed)
        return Response(status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TaskValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.title = serializer.validated_data['title']
        instance.description = serializer.validated_data['description']
        instance.completed = serializer.validated_data['completed']
        instance.save()
        return Response(status=status.HTTP_201_CREATED)