from django.shortcuts import render
from .serializers import TodosSerializer
from .models import Todos
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import permission_classes


# Create your views here.

class AuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True


class TodosAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        queryset = Todos.objects.filter(user=user)
        return queryset
    serializer_class = TodosSerializer


@permission_classes([permissions.IsAuthenticated, AuthorPermission])
class TodosUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


@permission_classes([permissions.IsAuthenticated, AuthorPermission])
class TodosDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

# nima gap