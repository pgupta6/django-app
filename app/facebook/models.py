from enum import unique

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    userId = models.CharField(max_length=255, unique=True)
    dob = models.DateField()

class Post(models.Model):
    """ Facebook post object """
    postId = models.AutoField(primary_key=True)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
    postString = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """ Facebook comment object """
    commentId = models.AutoField(primary_key=True)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
    postId = models.ForeignKey("Post", on_delete=models.CASCADE)
    commentString = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class PostToComment(models.Model):
    postId = models.ForeignKey("Post", on_delete=models.CASCADE)
    commentId = models.ForeignKey("Comment", on_delete=models.CASCADE)


class Item(models.Model):
    itemId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)


