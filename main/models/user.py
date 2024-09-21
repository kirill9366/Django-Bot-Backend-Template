from django.db import models


class TelegramUserModel(models.Model):
    account_id = models.BigIntegerField(
        verbose_name="ID аккаунта",
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    def __str__(self):
        return f"TelegramUser: {self.username or self.account_id}"