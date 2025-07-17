from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ConversationSerializer, MessageSerializer
from .models import Conversation, Message


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
