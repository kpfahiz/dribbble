from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    ''' This Serializer is used to  the LogIn of a user '''

    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to Authentication of a user '''
    
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff','auth_token')
         read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_auth_token(self, obj):
        token = Token.objects.get_or_create(user=obj)
        return token[0].key


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    class Meta:
        model = User
        fields = ('id', 'email','password', 'first_name', 'last_name')

class EmptySerializer(serializers.Serializer):
    pass