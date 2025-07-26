from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=225)
    phone_number = models.IntegerField()
    role = models.CharField(
        max_length=50,
        choices=[("admin", "Admin"), ("moderator", "Moderator"), ("clint", "Clint")],
        default="clint",
    )


class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )
    participants = models.ManyToManyField(User, related_name="conversations")
    StartedAt = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_body = models.CharField(max_length=225)
    status = models.CharField(
        max_length=50,
        choices=[("sent", "Sent"), ("delivered", "Delivered")],
        default="sent",
    )
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    conversation_id = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
