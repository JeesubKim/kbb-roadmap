from django import forms

from . import models


class CommentForm(forms.ModelForm):
    # id = forms.CharField(label="", max_length=100)
    # type = forms.CharField(label="", max_length=255)
    class Meta:

        model = models.Comment
        fields = ('comment', )
        exclude = ('author', )
