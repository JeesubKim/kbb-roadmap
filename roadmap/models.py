from django.db import models

from user import models as user_model
from django.contrib.auth import get_user_model
# Create your models here.
from kbb_roadmap.models import TimestamedModel

class Roadmap(TimestamedModel):
    
    roadmap_name = models.CharField(blank=False, max_length=100)
    status = models.CharField(blank=False, max_length=50)
    
    requester = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="roadmap_requester")
    assignee = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="roadmap_assignee")
    

class RoadmapAgreement(TimestamedModel):
    roadmap_id = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)


class RoadmapComplete(TimestamedModel):
    roadmap_id = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)


class RoadmapComments(TimestamedModel):
    author = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="roadmap_comment_author")
    roadmap = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE, related_name="roadmap")

    contents = models.TextField(blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name='comment_likes')