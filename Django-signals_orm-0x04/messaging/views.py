from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Message
from rest_framework.decorators import action
from rest_framework.response import Response


@login_required
def delete_user(request):
    if request.method == "DELETE":
        user = request.user
        if user:
            user.delete()
    return HttpResponse(status=200)


class MessageView(viewsets.ModelViewSet):

    def get_queryset(self):
        message_id = self.kwargs.get("message_pk")
        return (
            Message.objects.filter(pk=message_id)
            .select_related("sender", "parent_message")
            .prefetch_related("receiver", "replies")
        )

    # GET /messages/1/thread/
    @action(detail=True, methods=["get"])
    def thread(self, request, pk=None):
        message = self.get_object()
        thread = get_thread(message)
        return Response(thread)


def get_thread(message):
    return {
        "content": message.content,
        "replies": [get_thread(reply) for reply in message.replies.all()],
    }
