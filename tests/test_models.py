from datetime import date

from django.test import TestCase

from twitter.models import *


class TweetModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='larrypage', first_name='Larry', last_name='Page',
            email='lpage@google.com', birth_date=date(1992, 7, 6),
            password='password123')

    def test_image_tweets(self):
        """Should create a Tweet of type image when given url is valid"""
        self.assertEqual(Tweet.objects.count(), 0)
        image_tweet = ImageTweet.objects.create(image_url="http://images.com/1")
        Tweet.objects.create(
            user=self.user, content="Image tweet", media=image_tweet)
        self.assertEqual(Tweet.objects.count(), 1)
        tweet = Tweet.objects.first()
        self.assertEqual(tweet.type, 'image')

    def test_video_tweets(self):
        """Should create a Tweet of type video when given url is valid"""
        self.assertEqual(Tweet.objects.count(), 0)
        video_tweet = VideoTweet.objects.create(
            video_url="https://www.youtube.com/embed/video-id")
        Tweet.objects.create(
            user=self.user, content="Image tweet", media=video_tweet)
        self.assertEqual(Tweet.objects.count(), 1)
        tweet = Tweet.objects.first()
        self.assertEqual(tweet.type, 'video')

    def test_text_tweets(self):
        """Should create a Tweet of type text when no media is specified"""
        self.assertEqual(Tweet.objects.count(), 0)
        Tweet.objects.create(user=self.user, content="Image tweet")
        self.assertEqual(Tweet.objects.count(), 1)
        tweet = Tweet.objects.first()
        self.assertEqual(tweet.type, 'text')
