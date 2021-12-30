from rest_framework import serializers

from .models import Comment
from posts.serializers import PostListSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to create a comment '''
    
    class Meta:
        model = Comment
        fields = ['user', 'content', 'post']

class CommentDetailSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to get the details of a comment '''

    post = PostListSerializer()
    class Meta:
        model = Comment
        fields = ['content', 'post']
