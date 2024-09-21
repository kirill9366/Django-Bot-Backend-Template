from django.contrib import admin
from .models import TelegramUserModel, MessageModel


@admin.register(TelegramUserModel)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'username', 'created_at')
    search_fields = ('username', 'account_id')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'created_at')
    search_fields = ('key', 'value')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
