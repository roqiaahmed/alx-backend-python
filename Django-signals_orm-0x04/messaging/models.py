from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UnreadMessagesManager


class User(AbstractUser):
    email = models.EmailField(verbose_name="email address", max_length=225, unique=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ManyToManyField(User)
    content = models.TextField(null=False)
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = UnreadMessagesManager()


class Notification(models.Model):
    status = models.CharField(
        choices=[("read", "READ"), ("unread", "UNREAD")], default="unread"
    )
    notification_message = models.CharField(max_length=225)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    old_messages = models.TextField(null=False)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(auto_now_add=True)
