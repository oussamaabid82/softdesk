from django import forms
from django.db import models
from django.conf import settings

class Project(models.Model):
    project_id = models.IntegerField(auto_created=True)
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    type = models.CharField(max_length=100)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Contributor(models.Model):
    user_id = models.IntegerField(auto_created=True)
    project_id = models.IntegerField()
    permission = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

class Issue(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    tag = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    project_id = models.IntegerField()
    status = models.CharField(max_length=500)
    author_user_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_id = models.IntegerField(auto_created=True)
    description = models.CharField(max_length=8000)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
