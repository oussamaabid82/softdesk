from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Projects
from . serializers import ProjectSerializer


class ProjectAPIView(APIView):
    def get(self, *args, **kwargs):
        projects = Projects.objects.all()
        serialize = ProjectSerializer(projects, many=True)
        return Response(serialize.data)