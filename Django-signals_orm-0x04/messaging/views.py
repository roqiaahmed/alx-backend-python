from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Message
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@login_required
def delete_user(request):
    if request.method == "DELETE":
        sender = request.user
        if sender:
            sender.delete()
        return HttpResponse(status=200)


class MessageView(viewsets.ModelViewSet):

    def get_queryset(self):
        return (
            Message.objects.select_related("sender", "parent_message")
            .prefetch_related("receiver", "replies")
            .filter(
                models.Q(sender=self.request.user)
                | models.Q(receiver=self.request.user)
            )
        )

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # GET /messages/1/thread/
    @action(detail=True, methods=["get"])
    def thread(self, request, pk=None):
        message = self.get_object()
        thread = get_thread(message)
        return Response(thread)

    # GET /messages/unread/
    @action(
        detail=False, methods=["get"], url_path="unread"
    )  # detail=False becouse it will return list not a singel value
    def unread_inbox(self, request):
        user = request.user
        unread_messages = Message.unread.unread_for_user(user).only(
            "id", "content", "timestamp"
        )
        return Response(unread_messages.values("id", "content", "timestamp"))


def get_thread(message):
    return {
        "content": message.content,
        "replies": [get_thread(reply) for reply in message.replies.all()],
    }
