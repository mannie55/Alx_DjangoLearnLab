from .models import Post, Comment
from rest_framework import serializers
from django.conf import settings



class PostSerializer(serializers.ModelSerializer):
     # If you want to display the author's username instead of ID
      # Use this if you have __str__ method defined in your User model
    author = serializers.StringRelatedField() 

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']


    def validate_title(self, value):
        #validation to ensure title is not empty and has a reasonable length
        if not value:
            raise serializers.ValidationError('Title cannot be empty.')
        if len(value) < 5:
            raise serializers.ValidationError('Title must be atleast 5 characters long.')
        return value
    
    def validate_content(self, value):
        """Ensure content is not empty."""
        if not value:
            raise serializers.ValidationError("Content cannot be empty.")
        return value
    

class CommentSerializer(serializers.ModelSerializer):
    # Again, using StringRelatedField to display the author's username
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']


    def validate_content(self, value):
        """Ensure comment content is not empty."""
        if not value:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value


