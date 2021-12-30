from django.http import request
from django.db.models import Q

from rest_framework.generics import (
                            CreateAPIView,
                            ListAPIView,
                            RetrieveAPIView,
                            RetrieveUpdateAPIView,
                            DestroyAPIView
                    )
from rest_framework.filters import (
                            SearchFilter,
                            OrderingFilter
                    )       
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

from .models import Post
from .serializers import (
                PostCreateSerializer,
                PostListSerializer,
                PostDetailSerializer,
                AutherCreateSerializer,
                PostLikeSerializer,
                )

class AuthorCreateView(CreateAPIView):
    ''' This View Used to Create an author '''

    queryset = Post.objects.all()
    serializer_class = AutherCreateSerializer

class PostCreateView(CreateAPIView):
    ''' This view to Create a Post for logged in user '''

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostListView(ListAPIView):
    ''' This View List The all Post , Search Posts and Ordering Posts 
        Here Two types of Filters are used:
            1. SearchFilter
            2. QueryFilter                  '''

    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'timestamp']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                            Q(title__icontains=query) |
                            Q(content__icontains=query) |
                            Q(timestamp__icontains=query)
                            ).distinct()
        return queryset_list

class PostDetailView(RetrieveAPIView):
    ''' This View used to get Detail The Post '''

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateView(RetrieveUpdateAPIView):
    ''' This View used to Update The Post '''

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostDeleteView(DestroyAPIView):
    ''' This View used to Delete The Post '''

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

class PostLikeView(ListAPIView):
    ''' This View used to Like The Post '''

    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated]

    