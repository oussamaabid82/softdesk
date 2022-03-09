from django.db import models
from django.conf import settings

PRIORITY_CHOICES = [
    ('faible', 'FAIBLE'),
    ('moyen', 'MOYENNE'),
    ('elevee', 'ÉLEVÉE')
]

TAG_CHOICES = [
    ('bug', 'BUG'),
    ('amélioration', 'AMELIORATION'),
    ('tâche', 'TACHE'),    
]

STATUS_CHOICES = [
    ('à faire', 'A FAIRE'),
    ('en cours', 'EN COURS'),
    ('terminé', 'TERMINE'),
]

class Project(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    type = models.CharField(max_length=100)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Contributor(models.Model):
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

class Issue(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    tag = models.CharField(max_length=100, choices=TAG_CHOICES)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=500, choices=STATUS_CHOICES)
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    description = models.CharField(max_length=8000)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    create_time = models.DateTimeField(auto_now_add=True)
