from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Project, Contributor, Issue, Comment


class IssueListSerializer(ModelSerializer):
    
    class Meta:
        model = Issue
        fields = [
            'ip',
            'titel',
            'description',
            'project',
            'create_time'
            ]


class IssueDetailSerializer(ModelSerializer):
   
    class Meta:
        model = Issue
        fields = [
            'ip',
            'author_user',
            'assignee_user',
            'titel',
            'description',
            'project',
            'tag',
            'priority',
            'status',
            'create_time',
            ]
        depth = 1


class ProjectListSerializer(ModelSerializer):
   
    class Meta:
        model = Project
        fields = [
            'ip',
            'titel',
            'type',
            'description',
            'create_time'
            ]


class ProjectDetailSerializer(ModelSerializer):
    issues = IssueListSerializer(many=True)
        
    class Meta:
        model = Project
        fields = [
            'ip',
            'author_user',
            'titel',
            'type',
            'description',
            'issues',
            'create_time'
            ]
        depth = 1
               

class CommentListSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
            'ip',
            'author_user',
            'description',
            'create_time'
            ]    

class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'author_user',
            'issue',
            'description',
            'created_time'
            ]


class ContributorSerializer(ModelSerializer):  

    class Meta:
        model = Contributor 
        fields = [
            'ip',
            'author_user'      
            'permission',
            'role',
            ]
