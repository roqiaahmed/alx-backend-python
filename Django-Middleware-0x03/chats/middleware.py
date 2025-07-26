import logging
from django.http import HttpResponseForbidden
from datetime import datetime, timedelta
from ipware import get_client_ip


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
        is_message_view = is_path(request, "conversation_messages")
        if is_message_view and not "18:00" <= current_time <= "21:00":
            return HttpResponseForbidden("Can't access at that time")
        response = self.get_response(request)
        return response


def is_path(request, view_name):
    if hasattr(request, "resolver_match") and hasattr(request.resolver_match, "func"):
        view_func = request.resolver_match
        if hasattr(view_func, "view_name"):
            if view_func.view_name.startswith(view_name):
                return True
    return False


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.tracking = {"reset_time": "", "count": 0}

    def __call__(self, request):

        client_id = self.get_user_ip(request)
        if request.method == "POST" and is_path(request, "conversation_messages"):
            if not self.tracking_client_id(client_id):
                return HttpResponseForbidden("Pass messages limit")
        response = self.get_response(request)
        return response

    def tracking_client_id(self, client_id):
        curr_time = datetime.now()
        if (
            client_id in self.tracking
            and curr_time <= self.tracking[client_id]["reset_time"]
        ):
            if self.tracking[client_id]["count"] < 5:
                self.tracking[client_id]["count"] = +1
            else:
                return False
        else:
            self.tracking[client_id]["reset_time"] = curr_time + timedelta(minutes=1)
            self.tracking[client_id]["count"] = 1
        return True

    def get_user_ip(self, request):
        # x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        # if x_forwarded_for:
        #     # The header can contain a comma-separated list of IP addresses.
        #     # The first IP is typically the client's.
        #     ip = x_forwarded_for.split(",")[0]
        # else:
        #     # If no X-Forwarded-For header, fall back to REMOTE_ADDR.
        #     ip = request.META.get("REMOTE_ADDR")
        ip = get_client_ip(request)
        return ip
