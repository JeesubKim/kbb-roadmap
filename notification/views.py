from django.shortcuts import render, get_object_or_404

from kbb_roadmap.views import is_authenticated
# Create your views here.

from .models import Notification, NotificationStatus
from django.contrib.auth import get_user_model

def main(request):
    is_authenticated(request)

    
    notification_status = NotificationStatus.objects.filter(user_id=request.user.id)

    print(notification_status)

    context = {

        "notifications":notification_status
    }

    return render(request, "notification/notification.html", context)
    


