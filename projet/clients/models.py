from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES_CHOICES = [
    ("AUTHOR", "Auther"),
    ("CONTRIBUTOR", "Contributor"),    
]

class Client(AbstractUser):

    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'
    role = models.CharField(max_length=50, choices=ROLES_CHOICES)