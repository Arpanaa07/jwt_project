from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

def validate(self, attrs):
    email = attrs.get('email')
    password = attrs.get('password')
    
    users = User.objects.filter(email=email)
    if not users.exists():
        raise serializers.ValidationError("No user with this email.")
    
    user = users.first()

    print(f"Email entered: {email}")
    print(f"Password entered: {password}")
    print(f"User password hash: {user.password}")
    print(f"Password check result: {user.check_password(password)}")

    if not user.check_password(password):
        raise serializers.ValidationError("Incorrect password.")

    attrs['user'] = user
    return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()  

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
