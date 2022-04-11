from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

from .models import User


 
class UserSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['pk','username','first_name', 'last_name', 'email', 'password']

    # encode password
    def validate_password(self, value: str) -> str:
        return make_password(value)

    def validate(self, data):
        symbols_list = ('/\'\\=:;?!*+$£µ%')

        for symbol in symbols_list:
            if str(symbol) in data['email'] or str(symbol) in data['first_name'] or str(symbol) in data['last_name']:
                raise ValidationError('Symbol detected.')
        return data


class UserListSerializer(ModelSerializer):
    
    class Meta():
        model = User
        fields = [
            'pk', 
            'username',
            'password',
            'first_name', 
            'last_name', 
            'email'
            ]
 