from ..models import MessageModel
from ..serializers import MessageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters


class ListCreateMessageAPIView(ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = MessageModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['key', 'created_at']
    search_fields = ['key', 'value']


class RetrieveUpdateDestroyMessageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
