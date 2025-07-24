import logging


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
