from rest_framework.serializers import ModelSerializer

from .models import Project, Contributor, Issue, Comment


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'titel',
            'description',
            'tag',
            'priority',
            'status',
            'create_time'
        ]


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'author_user',
            'assignee_user',
            'titel',
            'description',
            'tag',
            'priority',
            'status',
            'create_time',
        ]
        # depth = 1


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'titel',
            'type',
            'description',
            'create_time'
        ]


class ProjectDetailSerializer(ModelSerializer):
    issues_project = IssueListSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'author_user',
            'contributors',
            'titel',
            'type',
            'description',
            'issues_project',
            'create_time'
        ]
        depth = 1


class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
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
            'id',
            'user',
            'permissions',
            'role',
        ]
