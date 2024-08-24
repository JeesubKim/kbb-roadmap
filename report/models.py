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


# class ReportComment(TimestamedModel):
#     author = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)
#     report = models.ForeignKey(Report, null=False, on_delete=models.CASCADE)
#     comment = models.TextField(blank=True)
    


# class ReportCommentLikes(TimestamedModel):
#     user = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)
#     comment = models.ForeignKey(ReportComment, null=False, on_delete=models.CASCADE)