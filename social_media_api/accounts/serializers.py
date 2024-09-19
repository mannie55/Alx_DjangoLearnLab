from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture']


    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            bio=validated_data.get('bio', 'not set'),
            profile_picture=validated_data.get('profile_picture', 'No profile picture')
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture']
        #to prevent updates to this fields
        read_only_fields = ['id', 'username', 'followers']

    def  update(self, instance, validated_data):
        return super().update(instance, validated_data)