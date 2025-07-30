from django.db import models


class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        return super().get_queryset().filter(receiver=user, is_read=False)
