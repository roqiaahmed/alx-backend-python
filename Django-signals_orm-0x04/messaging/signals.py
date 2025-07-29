from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Message, Notification, MessageHistory


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


@receiver(pre_save, sender=Message)
def update_message(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        original = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return
    if original.content != instance.content:
        instance.edited = True

        MessageHistory.objects.create(
            message=instance,
            old_messages=original.content,
            edited_by=instance.sender,
        )

        messages_H = MessageHistory.objects.filter(message=instance)
        for old_message in messages_H:
            print(old_message.old_messages)
