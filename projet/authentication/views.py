from rest_framework.viewsets import ModelViewSet

from .models import Users
from .serializers import UserListSerializer, UserSerializer


class UserListViewset(ModelViewSet):

    serializer_class = UserListSerializer

    def get_queryset(self):
        return Users.objects.all()


class SignupViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return[]
