from django.db import models
from django.conf import settings


class Project(models.Model):
    TYPE_CHOICES = [
        ('back-end', 'BACK-END'),
        ('front-end', 'FRONT-END'),
        ('iOS', 'iOS'),
        ('android', 'ANDROID')
    ]

    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='project_author', 
        null=True
    )
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Contributor',
        related_name='contributions'
    )  
    create_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    
    ROLES_CHOICES = [
        ("AUTHOR", "Auther"),
        ("CONTRIBUTOR", "Contributor"),    
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='contributor_project', null=True)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributor_user')
    permission = models.CharField(max_length=50, choices=ROLES_CHOICES)
    role = models.CharField(max_length=100, choices=ROLES_CHOICES)

    class Meta:
        unique_together = ('author_user', 'project')


class Issue(models.Model):
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

    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=8000)
    tag = models.CharField(max_length=100, choices=TAG_CHOICES)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues_project')
    status = models.CharField(max_length=500, choices=STATUS_CHOICES)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_author')
    assignee_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_assignee', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):
    description = models.CharField(max_length=8000)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comment_issue')
    create_time = models.DateTimeField(auto_now_add=True)
