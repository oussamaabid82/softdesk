from django.db import models
from django.conf import settings

class Project(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    type = models.CharField(max_length=100)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Contributor(models.Model):
    project_id = models.IntegerField()
    permission = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

class Issue(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    tag = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=500)
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    description = models.CharField(max_length=8000)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
