from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Use create_user method to handle user creation
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', 'not set'),
            profile_picture=validated_data.get('profile_picture', None)
        )
        
        # Create and assign token to the new user
        Token.objects.create(user=user)
        
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'bio', 'profile_picture']
        #to prevent updates to this fields
        read_only_fields = ['id', 'username', 'followers']

    def  update(self, instance, validated_data):
        return super().update(instance, validated_data)