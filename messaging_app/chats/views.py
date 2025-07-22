from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer
from .models import Conversation, Message, User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsParticipantOfConversation, IsParticipantInConversation
from django.core.exceptions import PermissionDenied
from .pagination import MessagesPagination
from .filters import MessageFilter


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConversationViewSet(viewsets.ModelViewSet):

    serializer_class = ConversationSerializer
    permission_classes = [
        IsAuthenticated,
        IsParticipantOfConversation,
    ]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Response("UnAuthenticated", status=status.HTTP_403_FORBIDDEN)
        return Conversation.objects.filter(participants=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantInConversation]
    pagination_class = [MessagesPagination]
    filterset_class = [MessageFilter]

    def get_queryset(self):
        conversation = self.get_conversation()
        return Message.objects.filter(conversation_id=conversation)

    def perform_create(self, serializer):
        conversation = self.get_conversation()
        serializer.save(conversation_id=conversation, sender=self.request.user)

    def get_conversation(self):
        conversation_id = self.kwargs.get("conversation_pk")
        conversation = get_object_or_404(Conversation, pk=conversation_id)
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not allowed to access this conversation.")
        return conversation
