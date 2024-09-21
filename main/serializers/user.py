from rest_framework import serializers
from ..models import TelegramUserModel


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        fields = "__all__"
