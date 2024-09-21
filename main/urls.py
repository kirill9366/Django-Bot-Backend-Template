from django.urls import path
from .views import (
    ListCreateMessageAPIView,
    RetrieveUpdateDestroyMessageAPIView,
    ListCreateTelegramUserAPIView,
    RetrieveUpdateDestroyTelegramUserAPIView,
)

urlpatterns = [
    # Routes for MessageModel
    path('messages/', ListCreateMessageAPIView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', RetrieveUpdateDestroyMessageAPIView.as_view(), name='message-retrieve-update-destroy'),

    # Routes for TelegramUserModel
    path('users/', ListCreateTelegramUserAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', RetrieveUpdateDestroyTelegramUserAPIView.as_view(), name='user-retrieve-update-destroy'),
]
