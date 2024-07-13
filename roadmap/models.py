from django.db import models

from user import models as user_model

# Create your models here.

class TimestamedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        abstract = True

class Roadmap(TimestamedModel):
    
    roadmap_name = models.CharField(blank=False, max_length=100)
    status = models.CharField(blank=False, max_length=50)
    requester = models.ForeignKey(user_model.User, null=False, on_delete=models.CASCADE, related_name="roadmap_requester")
    assignee = models.ForeignKey(user_model.User, null=False, on_delete=models.CASCADE, related_name="roadmap_assignee")
    

class RoadmapAgreement(TimestamedModel):
    roadmap_id = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_model.User, null=False, on_delete=models.CASCADE)


class RoadmapComplete(TimestamedModel):
    roadmap_id = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_model.User, null=False, on_delete=models.CASCADE)


class RoadmapComments(TimestamedModel):
    author = models.ForeignKey(user_model.User, null=False, on_delete=models.CASCADE, related_name="roadmap_comment_author")
    roadmap = models.ForeignKey(Roadmap, null=False, on_delete=models.CASCADE, related_name="roadmap")

    contents = models.TextField(blank=True)
    likes = models.ManyToManyField(user_model.User, related_name='comment_likes')