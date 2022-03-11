from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated

from . models import Issue, Project, Comment, Contributor
from . serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContibutorSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    
    def get_queryset(self, request):
        Project.contributors.add(request.user)
        return Project.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    
    def get_queryset(self):
        return Issue.objects.all()

    def post_issue(self, request, pk):
        if request.user in Contributor.author_user:
            print('HELLO')
            

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.all()


class ContibutorViewSet(ReadOnlyModelViewSet):
    serializer_class = ContibutorSerializer
    def get_queryset(self):
        return Comment.objects.all()
