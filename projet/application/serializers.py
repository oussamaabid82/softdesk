from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment



class ContibutorSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor 
        fields = ['author_user', 'project','permission', 'role']

class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue', 'create_time']

class IssueSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Issue
        fields = ['id', 'titel', 'description', 'create_time', 'comments']    

class ProjectSerializer(ModelSerializer):
    issues = IssueSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id', 'titel', 'description', 'type', 'author_user', 'create_time', 'issues']
