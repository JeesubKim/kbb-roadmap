from django import forms

from . import models

class RoadmapNameForm(forms.Form):
    roadmap_name = forms.CharField(label="로드맵", max_length=50)
    assignee = forms.CharField(label="담당자", max_length=15)
    


# class RoadmapCommentForm(forms.ModelForm):

#     class Meta:

#         model = models.RoadmapComment
#         fields = ('comment', )
#         exclude = ('author', )
