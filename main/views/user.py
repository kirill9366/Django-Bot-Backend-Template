from ..models import TelegramUserModel
from ..serializers import TelegramUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters


class ListCreateTelegramUserAPIView(ListCreateAPIView):
    serializer_class = TelegramUserSerializer
    queryset = TelegramUserModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['account_id', 'username', 'created_at']
    search_fields = ['username', 'account_id']


class RetrieveUpdateDestroyTelegramUserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TelegramUserModel.objects.all()
    serializer_class = TelegramUserSerializer
