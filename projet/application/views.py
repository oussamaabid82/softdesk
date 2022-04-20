from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.db.models import Q

from . models import Issue, Project, Comment, Contributor
from . serializers import (
    IssueDetailSerializer, ProjectDetailSerializer,
    IssueListSerializer, CommentListSerializer, CommentDetailSerializer,
    ContributorSerializer, ProjectListSerializer
)
from .permissions import IsAdminAuthenticated, IsContributor


class MultipleSerializerMixin:
    # créer une liaison dans l'url en utilisant le "id" entre project, issue et comment
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    permission_classes = [IsContributor]
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        # Afficher les projets que l'utilisateur connécter est designé comme contributor
        return Project.objects.filter(contributors=self.request.user)

    def perform_create(self, serializer):
        # lier l'utilsateur connecter au projet créer
        project = serializer.save(author_user=self.request.user)

        # Créer contributor en mettant l'utilisateur connecter comme auth_user
        Contributor.objects.create(
            user=self.request.user,
            project=project,
            permissions='AUTHOR',
            role=''
        )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewset(ModelViewSet):
    permission_classes = [IsAdminAuthenticated]

    serializer_class = ContributorSerializer

    def get_queryset(self):
        # Vérifier si l'utilisateur est contributor ou non
        try:
            contributor_exist = Contributor.objects.get(
                Q(project=self.kwargs['project_pk']) & Q(user=self.request.user)
            )
            if contributor_exist:
                return Contributor.objects.filter(project=self.kwargs['project_pk'])

        except Contributor.DoesNotExist:
            print('Aucun résultat.')

    def perform_create(self, serializer):
        # Recupérer le 'id' du projet puis lier ce projet au contributor
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        serializer.save(project=project)


class IssueViewSet(ModelViewSet):
    permission_classes = [IsAdminAuthenticated]
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        # Recupérer le 'id' du projet
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])

        # lorsque l'utillisateur connécter céer un issue il en est automatiquement auther_user et assignee
        serializer.save(project=project, author_user=self.request.user, assignee_user=self.request.user)

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
        # Recupérer le 'id' du issue
        issue = get_object_or_404(Issue, id=self.kwargs['issue_pk'])

        # lorsque l'utillisateur connécter céer un comment il en est automatiquement auther_user
        serializer.save(
            author_user=self.request.user,
            issue=Issue.objects.get(pk=self.kwargs['issue_pk'])
        )
