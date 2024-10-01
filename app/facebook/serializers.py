"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from facebook.models import User, Comment, Post, PostToComment, Item


class FBUserSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = User
        fields = ['userId', 'name', 'email', 'dob']
        #read_only_fields = ['userId']


class PostSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Post
        fields = ['userId', 'postId', 'postString', 'timestamp']
        #read_only_fields = ['userId', 'postId']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Comment
        fields = ['userId', 'commentId', 'postId', 'commentString', 'timestamp']
        #read_only_fields = ['userId', 'commentId']

class PostToCommentSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = PostToComment
        fields = ['postId', 'commentId']
        #read_only_fields = ['postId', 'commentId']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemId', 'name', 'description', 'price']
