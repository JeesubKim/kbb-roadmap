from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from kbb_roadmap.views import is_authenticated
# Create your views here.

from .models import Notification, NotificationStatus

def main(request):
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')

    
    notification_status = NotificationStatus.objects.filter(user_id=request.user.id)

    notis = list(notification_status)
    
    
    context = {

        "notifications":[ 
            { "notification_name": noti.notification.notification_name,
            "notification_content": noti.notification.notification_content,
            "notification_type" : noti.notification.notification_type,
            "notification_link" : noti.notification.notification_link 
            } for noti in notis 
            
            ] 
    }

    return render(request, "notification/notification.html", context)
    





def create_notification(notification):
    name = notification.get("name", "")
    content = notification.get("content", "")
    type = notification.get("type", "")
    link = notification.get("link", "")

    if name == "" or content == "" or type == "" or link == "":
        return
    
    new_notification = Notification.objects.create(
        notification_name = name,
        notification_content = content,
        notification_type = type,
        notification_link = link
    )

    new_notification.save()
    users = list(get_user_model().objects.all())
    
    for user in users:

        noti_status = NotificationStatus.objects.create(
            notification = new_notification,
            user = user,
            is_read = False
        )
        noti_status.save()
