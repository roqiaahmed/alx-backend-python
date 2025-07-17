from django.urls import path
from .views import ConversationViewSet, MessageViewSet


urlpatterns = [
    path("conversation/", ConversationViewSet.as_view(), name="conversation"),
    path("message/", MessageViewSet.as_view(), name="message"),
]
