from django.forms import ChoiceField
from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['__all__']

class ContibutorSerializer(ModelSerializer):
    permission = ChoiceField()
    
    class Meta:
        model = Contributor 
        field = ['__all__']

class IssueSerializer(ModelSerializer):
    
    class Meta:
        model = Issue
        field = ['__all__']

class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        field = ['__all__']