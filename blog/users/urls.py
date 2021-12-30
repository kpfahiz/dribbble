from django.contrib import admin
from django.urls import path, include

from .views import AuthViewSet

urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'})),
    path('register/', AuthViewSet.as_view({'post': 'register'})),
    path('logout/', AuthViewSet.as_view({'post': 'logout'})),
]