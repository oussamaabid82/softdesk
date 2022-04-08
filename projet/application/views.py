from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from . models import Issue, Project, Comment, Contributor
from . serializers import (
    IssueDetailSerializer, ProjectDetailSerializer, 
    IssueListSerializer,CommentListSerializer, CommentDetailSerializer,
    ContributorSerializer, ProjectListSerializer
    )
from .permissions import IsAdminAuthenticated 

"""
Mixin : Display detail of object
Ex : projects/{id}/
""" 
class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Display all project if logged user is contributor
        return Project.objects.filter(contributors=self.request.user)
    
    def perform_create(self, serializer):
        # Save project with the current logged user
        project = serializer.save(author_user=self.request.user)
        
        Contributor.objects.create(
            auth_user=self.request.user,
            project=project,
            permissions='AUTHOR',
            role=''
        )
        
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        # Check if logged user is contributor
        try:
            contributor_exist = Contributor.objects.get(
                Q(project=self.kwargs['project_pk']) & Q(author_user=self.request.user)
            )
            if contributor_exist:
                return Contributor.objects.filter(project=self.kwargs['project_pk'])

        except Contributor.DoesNotExist:
            print('Aucun résultat.')

    def perform_create(self, serializer):
        # get project object projects/{id}/
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        # save contributor information with the current projects/{id}/
        serializer.save(project=project)
    
    
class IssueViewSet(ModelViewSet):
    permission_classes = [IsAdminAuthenticated]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    
    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_pk'])
    
    def perform_create(self, serializer):
        serializer.save(
            project=Project.objects.get(pk=self.kwargs['project_pk']), 
            author_user=self.request.user,
            assignee_user=self.request.user
            )
       
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
        

class CommentViewSet(ModelViewSet):
    permission_classes = [IsAdminAuthenticated]
    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
       
    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_pk'])

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user, issue=Issue.objects.get(pk=self.kwargs['issue_pk']))
