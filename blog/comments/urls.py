from django.contrib import admin
from django.urls import path, include

from .views import CommentDetailView, CommentCreateView

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('<int:pk>/', CommentDetailView.as_view(), name='detail'),
]
