from rest_framework.viewsets import ReadOnlyModelViewSet

from . models import Client
from . serializers import ClientSerializer

class ClientViewSet(ReadOnlyModelViewSet):
    serializer_class = ClientSerializer
    def get_queryset(self):
        return Client.objects.all()