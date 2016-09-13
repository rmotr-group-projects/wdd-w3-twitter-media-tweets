from django import forms

from .models import Tweet


class TweetForm(forms.Form):
    content = forms.CharField(max_length=140)
    image_url = forms.URLField(required=False)
    video_url = forms.URLField(required=False)
