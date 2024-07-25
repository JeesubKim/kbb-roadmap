from django import forms

class RoadmapNameForm(forms.Form):
    roadmap_name = forms.CharField(label="로드맵 제목", max_length=15)
    assignee = forms.CharField(label="Assignee", max_length=15)
