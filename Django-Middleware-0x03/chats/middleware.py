import logging
from django.http import HttpResponseForbidden
from datetime import datetime


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user
        if user.username:
            self.logger.debug(f"- User: {request.user.username} - Path: {request.path}")
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")

        response = self.get_response(request)
        if hasattr(request, "resolver_match") and hasattr(
            request.resolver_match, "func"
        ):
            view_func = request.resolver_match
            if hasattr(view_func, "view_name"):
                if (
                    view_func.view_name.startswith("conversation_messages")
                    and not "18:00" <= current_time <= "21:00"
                ):
                    return HttpResponseForbidden("Can't access at that time")
        return response
