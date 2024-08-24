from django.db import models
from kbb_roadmap.models import TimestamedModel
from django.contrib.auth import get_user_model
from roadmap.models import Roadmap
from report.models import Report


class Comment(TimestamedModel):
    author = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="comment_author")
    comment = models.TextField(blank=True)

class CommentLikes(TimestamedModel):
    user = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)




class RoadmapComment(TimestamedModel):
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE, related_name="comment_for_roadmap")
    roadmap = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE)


class ReportComment(TimestamedModel):
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE, related_name="comment_for_report")
    report = models.ForeignKey(Report, null=False, on_delete=models.CASCADE)

