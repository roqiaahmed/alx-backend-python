from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message, Notification


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.sender
        receivers = instance.receiver.all()
        notification_message = f"Get new message from {user.username}"
        for receiver in receivers:
            Notification.objects.create(
                notification_message=notification_message,
                receiver=receiver,
                message=instance,
            )
