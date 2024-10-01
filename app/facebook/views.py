"""
Views for the recipe APIs
"""
import csv
from inspect import stack

from django.core.files.storage import default_storage
from django.template.defaulttags import comment
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from facebook.models import User, Comment, Post, PostToComment, Item
from facebook.serializers import (
    FBUserSerializer,
    PostSerializer,
    CommentSerializer,
    PostToCommentSerializer,
    ItemSerializer
)
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = FBUserSerializer
    queryset = User.objects.all()


    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return FBUserSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save()


class PostViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return PostSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""

        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(post=self.request.post).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return CommentSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save()


class PostToCommentViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = PostToCommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset

    # def get_serializer_class(self):
    #     """Return the serializer class for request."""
    #     if self.action == 'list':
    #         return PostToCommentSerializer
    #
    #     return self.serializer_class
    #
    # def perform_create(self, serializer):
    #     """Create a new recipe."""
    #     serializer.save()


# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()

class ItemCSVViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        print("Under create")
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_Valid():
            item_serializer.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Item Added Sucessfully", "status": status_code})









