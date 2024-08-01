from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



from kbb_roadmap.models import TimestamedModel


class Report(TimestamedModel):

    report_subject = models.CharField(blank=False, max_length=50)
    report_content = models.TextField(blank=True)
    report_image = models.ImageField(blank=False)
    # reporter = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="reporter", default="None")
    reporter = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="user")


class ReportStatus(TimestamedModel):
    report_id = models.ForeignKey(Report, null=False, on_delete=models.CASCADE)
    report_status = models.CharField(blank=False, max_length=20)
