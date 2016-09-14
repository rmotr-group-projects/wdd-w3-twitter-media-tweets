from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_validated = models.BooleanField(default=False)


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    content = models.CharField(max_length=140, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    media = GenericForeignKey('content_type', 'object_id')

    @property
    def type(self):
        if self.media:
            return self.content_type.model.replace('tweet', '')
        return "text"


class ImageTweet(models.Model):
    image_url = models.URLField()


class VideoTweet(models.Model):
    video_url = models.URLField()
