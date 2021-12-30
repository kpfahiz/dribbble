from rest_framework.generics import (
                            CreateAPIView,
                            RetrieveAPIView,
                    )       
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .serializers import (
                CommentCreateSerializer,
                CommentDetailSerializer,
                )



class CommentCreateView(CreateAPIView):
    ''' This view to Create a Comment for logged in user '''
    
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailView(RetrieveAPIView):
    ''' This View Get the Details of The Comment '''

    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer