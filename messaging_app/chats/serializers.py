from rest_framework import serializers
from .models import User, Message, Conversation
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "password",
            "phone_number",
            "username",
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data.get("email"),
            phone_number=validated_data.get("phone_number", ""),
            password=validated_data["password"],
        )
        return user


class MessageSerializer(serializers.ModelSerializer):
    message_body = serializers.CharField(
        max_length=225
    )  # used for input (post & update)
    preview = serializers.SerializerMethodField()  # used for output (get)

    class Meta:
        model = Message
        fields = [
            "message_id",
            "message_body",
            "preview",
            "status",
            "is_read",
            "sent_at",
            "created_at",
            "sender",
            "conversation_id",
        ]
        read_only_fields = [
            "message_id",
            "sender",
            "conversation_id",
            "sent_at",
            "created_at",
        ]

    def get_preview(self, obj):
        return obj.message_body[:30]

    def create(self, validated_data):
        sender = validated_data["sender"]
        conversation = validated_data["conversation_id"]

        # Check if sender is in the conversation participants
        if not conversation.participants.filter(id=sender.id).exists():
            raise PermissionDenied("You are not a participant in this conversation.")

        return super().create(validated_data)


class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            "conversation_id",
            "participants",
            "messages",
        ]
        read_only_fields = ["conversation_id", "started_at"]

    def create(self, validated_data):
        participants = validated_data.pop("participants")
        conversation = Conversation.objects.create(**validated_data)
        conversation.participants.set(participants)
        return conversation
