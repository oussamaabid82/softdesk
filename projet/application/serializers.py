from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment
from clients.serializers import ClientSerializer


class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue', 'create_time']


class IssueSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Issue
        fields = ['id','assignee_user', 'titel', 'description', 'create_time', 'comments']
 
    
class ProjectSerializer(ModelSerializer):
    issues = IssueSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id', 'titel', 'description', 'type', 'contributors', 'create_time', 'issues']


class ContibutorSerializer(ModelSerializer):
    author_user = ClientSerializer(many=True)
    class Meta:
        model = Contributor 
        fields = ['author_user', 'project','permission', 'role']
