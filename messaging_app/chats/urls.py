from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"conversations", ConversationViewSet, basename="conversation")

messages_router = NestedSimpleRouter(router, r"conversations", lookup="conversation")
router.register(r"messages", MessageViewSet, basename="conversation_messages")

urlpatterns = [path("", include(router.urls)), path("", include(messages_router.urls))]
