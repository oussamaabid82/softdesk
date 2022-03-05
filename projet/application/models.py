from django import forms
from django.db import models
from django.conf import settings

class Projects(models.Model):
    project_id = models.IntegerField()
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    type = models.CharField(max_length=100)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Contibutors(forms.Form):
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    permission = forms.ChoiceField()
    role = models.CharField(max_length=100)

class Issues(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    tag = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    project_id = models.IntegerField()
    status = models.CharField(max_length=500)
    author_user_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField()

class Comments(models.Model):
    comment_id = models.IntegerField()
    description = models.CharField(max_length=8000)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE)
    create_time = models.DateTimeField()
