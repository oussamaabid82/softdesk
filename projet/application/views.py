from rest_framework.viewsets import ModelViewSet

from . models import Projects
from . serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    
    serializer_class = ProjectSerializer
    
    def get_queryset(self, *args, **kwargs):
        return Projects.objects.all()