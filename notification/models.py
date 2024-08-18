from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from kbb_roadmap.models import TimestamedModel


class Notification(TimestamedModel):

    notification_name = models.CharField(blank=False, max_length=50)
    notification_content = models.CharField(blank=False, max_length=100)
    notification_type = models.CharField(blank=False, max_length=10)
    notification_link = models.TextField(blank=True)

    

class NotificationStatus(TimestamedModel):
    notification = models.ForeignKey(Notification, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)
    is_read = models.BooleanField(blank=False, default=False)

    