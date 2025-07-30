from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def delete_user(request):
    if request.method == "DELETE":
        curr_user = request.user
        if curr_user:
            User.objects.delete(pk=curr_user.id)
