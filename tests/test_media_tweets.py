from datetime import date

from django_webtest import WebTest
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from twitter.models import Tweet, ImageTweet, VideoTweet

User = get_user_model()


class MediaTweetsTestCase(WebTest):
    def setUp(self):
        self.user = User.objects.create_user(
            username='larrypage', first_name='Larry', last_name='Page',
            email='lpage@google.com', birth_date=date(1992, 7, 6),
            password='password123')

    def test_media_tweets(self):
        """Should """
        import ipdb; ipdb.set_trace()
        pass
