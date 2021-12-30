from rest_framework import serializers

from .models import Post, Author

class AutherCreateSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to create an author '''

    class Meta:
        model = Author
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to create a post '''

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')

class PostListSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to get the list of posts '''

    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author')
    
    def get_author(self, obj):
        return obj.author.user.email

class PostDetailSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to get the details of a post '''
    
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content',  'timestamp', 'categories', 'author')
    
    def get_author(self, obj):
        return obj.author.user.email
class PostLikeSerializer(serializers.ModelSerializer):
    ''' This Serializer is used to get the details of a post's likes '''
    
    author = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ( 'id', 'title', 'author', 'likes' )
    
    def get_author(self, obj):
        return obj.author.user.email
        
    def get_likes(self, obj):
        return obj.likes.all()