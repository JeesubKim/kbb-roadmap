from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, JsonResponse
from kbb_roadmap.views import is_authenticated
# Create your views here.

from .models import Notification, NotificationStatus

def main(request):
    # if not is_authenticated(request):
    #     return HttpResponseRedirect('/user/')

    
    notification_status = NotificationStatus.objects.filter(user_id=request.user.id).order_by("-created_at").order_by("is_read")
    
    notis = list(notification_status)
    
    
    context = {

        "notifications":[{ 
            "notification_id": noti.notification.pk,
            "notification_name": noti.notification.notification_name,
            "notification_content": noti.notification.notification_content,
            "notification_type" : noti.notification.notification_type,
            "notification_link" : noti.notification.notification_link,
            "created_at": noti.notification.created_at,
            "is_read":noti.is_read
            } for noti in notis ] 
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
    users = list(get_user_model().objects.filter(is_superuser=False))
    
    for user in users:

        noti_status = NotificationStatus.objects.create(
            notification = new_notification,
            user = user,
            is_read = False
        )
        noti_status.save()


def is_read(request, id):
    notis = Notification.objects.filter(pk=id)
    stat = NotificationStatus.objects.filter(notification = notis[0], user_id=request.user.id)
    stat.update(is_read=True)
    return JsonResponse({"success":True})