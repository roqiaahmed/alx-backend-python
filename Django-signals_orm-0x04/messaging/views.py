from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def delete_user(request):
    if request.method == "DELETE":
        user = request.user
        if user:
            user.delete()
    return HttpResponse(status=200)
