from rest_framework import filters


class MessageFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        message_body = request.query_params.get("message_body")
        if message_body:
            queryset = queryset.filter(message_body__icontains=message_body)
        return queryset
