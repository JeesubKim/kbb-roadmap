from django import forms
from . import models
class ReportForm(forms.Form):
    report_subject = forms.CharField(label="제목", max_length=100)
    report_content = forms.CharField(label="내용", max_length=255)
    report_image = forms.ImageField()


# class ReportCommentForm(forms.ModelForm):

#     class Meta:

#         model = models.ReportComment
#         fields = ('comment', )
#         exclude = ('author', )
