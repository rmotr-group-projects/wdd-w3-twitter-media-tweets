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

    MODELS = (models.Q(app_label='twitter', model='ImageTweet') |
              models.Q(app_label='twitter', model='VideoTweet'))

    class Meta:
        ordering = ['-created']

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    content = models.CharField(max_length=140, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    media_type = models.ForeignKey(ContentType,
                                   null=True,
                                   blank=True,
                                   limit_choices_to=MODELS,
                                   on_delete=models.CASCADE,
                                   verbose_name='Type')
    media_id = models.PositiveIntegerField(null=True,
                                           blank=True,
                                           verbose_name='Tweet Id')
    media = GenericForeignKey('media_type', 'media_id')


class ImageTweet(models.Model):
    image_url = models.URLField()


class VideoTweet(models.Model):
    video_url = models.URLField()
