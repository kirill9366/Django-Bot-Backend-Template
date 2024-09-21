from django.db import models


class MessageModel(models.Model):
    key = models.CharField(
        max_length=255,
        verbose_name="Ключ сообщения",
    )
    value = models.CharField(
        verbose_name="Значение сообщения",
        max_length=4000,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.key
