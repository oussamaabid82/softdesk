from xml.etree.ElementTree import Comment
from rest_framework.viewsets import ReadOnlyModelViewSet

from . models import Issue, Project, Comment
from . serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        return Project.objects.all()

class IssueViewSet(ReadOnlyModelViewSet):
    serializer_class = IssueSerializer
    def get_queryset(self):
        return Issue.objects.all()

class CommentViewSet(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.all()