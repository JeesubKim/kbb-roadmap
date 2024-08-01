from django import forms

class ReportForm(forms.Form):
    report_subject = forms.CharField(label="제목", max_length=100)
    report_content = forms.CharField(label="내용", max_length=255)
    report_image = forms.ImageField()

