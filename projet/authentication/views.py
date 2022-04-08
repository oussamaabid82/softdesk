from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserListSerializer, UserSerializer


class UserListViewset(ModelViewSet):

    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()


class SignupViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return[]