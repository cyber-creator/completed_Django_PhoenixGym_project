from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets
# Create your views here.
from .permissions import IsAuthorOrReadOnly, IsCoachOrReadOnly
from apiblog.serializers import BlogSerializer, UsersSerializer
from gym.models import Blog, BlogCategory


class BlogsAPIViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, IsCoachOrReadOnly)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UsersAPIViewsSets(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer
