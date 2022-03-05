from rest_framework.serializers import ModelSerializer
from .models import Projects, Issues, Comments


class ProjectSerializer(ModelSerializer):
    
    class Meta:
        model = Projects
        fields = ['project_id', 'titel', 'description', 'type', 'author_user_id']     

        