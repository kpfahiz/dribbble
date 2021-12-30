from django.contrib import admin
from django.urls import path, include

from .views import(
            PostListView,
            PostDetailView,
            PostCreateView,
            PostUpdateView,
            PostDeleteView,
            AuthorCreateView,
            PostLikeView,
            )

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('listall/', PostListView.as_view(), name='listall'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('like/', PostLikeView.as_view(), name='like'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
]   
