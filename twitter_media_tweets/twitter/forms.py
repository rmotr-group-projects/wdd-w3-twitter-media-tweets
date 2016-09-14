from django import forms

from .models import Tweet


class TweetForm(forms.Form):
    content = forms.CharField(max_length=140)
    image_url = forms.URLField(required=False)
    video_url = forms.URLField(required=False)

    def clean_video_url(self):
        data = self.cleaned_data['video_url']
        if data and "https://www.youtube.com/embed/" not in data:
            raise forms.ValidationError("Your video url needs to be in the format \"https://www.youtube.com/embed/id\"")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data