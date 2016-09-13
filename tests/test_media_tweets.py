from datetime import date

from django_webtest import WebTest

from twitter.models import *


class MediaTweetsTestCase(WebTest):
    def setUp(self):
        self.user = User.objects.create_user(
            username='larrypage', first_name='Larry', last_name='Page',
            email='lpage@google.com', birth_date=date(1992, 7, 6),
            password='password123')

    def test_text_tweets(self):
        """Should create a Tweet of type text when no media is specified"""
        # Preconditions
        self.assertEqual(Tweet.objects.count(), 0)

        feed = self.app.get('/larrypage', user=self.user)
        self.assertTrue(
            "<strong>@larrypage</strong> hasn't tweeted yet :(" in str(feed.html))
        form = feed.form
        form['content'] = 'Testing TEXT tweets'
        form.submit()

        # Postconditions
        self.assertEqual(Tweet.objects.count(), 1)

        tweet = Tweet.objects.first()
        self.assertEqual(tweet.type, 'text')

        feed = self.app.get('/larrypage', user=self.user)
        self.assertFalse(
            "<strong>@larrypage</strong> hasn't tweeted yet :(" in str(feed.html))
        tweet_content = feed.html.find('div', class_='tweet-content').text
        self.assertEqual(tweet_content, 'Testing TEXT tweets')

    def test_image_tweets(self):
        """Should create a Tweet of type image when given url is valid"""
        # Preconditions
        self.assertEqual(Tweet.objects.count(), 0)

        feed = self.app.get('/larrypage', user=self.user)
        self.assertTrue(
            "<strong>@larrypage</strong> hasn't tweeted yet :(" in str(feed.html))
        form = feed.form
        form['content'] = 'Testing IMAGE tweets'
        form['image_url'] = 'http://images.com/1'
        form.submit()

        # Postconditions
        self.assertEqual(Tweet.objects.count(), 1)

        tweet = Tweet.objects.first()
        self.assertEqual(tweet.type, 'image')

        feed = self.app.get('/larrypage', user=self.user)
        self.assertFalse(
            "<strong>@larrypage</strong> hasn't tweeted yet :(" in str(feed.html))
        tweet_content = feed.html.find('div', class_='tweet-content').text
        tweet_image_url = feed.html.find('img', class_='tweet-image')['src']
        self.assertEqual(tweet_content, 'Testing IMAGE tweets')
        self.assertEqual(tweet_image_url, 'http://images.com/1')

    def test_video_tweets(self):
        """Should create a Tweet of type video when given url is valid"""
        # Preconditions
        self.assertEqual(Tweet.objects.count(), 0)

        feed = self.app.get('/larrypage', user=self.user)
        self.assertTrue(
            "<strong>@larrypage</strong> hasn't tweeted yet :(" in str(feed.html))
        form = feed.form
        form['content'] = 'Testing VIDEO tweets'
        form['video_url'] = 'https://www.youtube.com/embed/video-id'
        form.submit()

        # Postconditions
        self.assertEqual(Tweet.objects.count(), 1)

        tweet = Tweet.objects.first()
        self.assertEqual(tweet.type, 'video')

        feed = self.app.get('/larrypage', user=self.user)
        self.assertFalse(
            "<strong>@larrypage</strong> hasn't tweeted yet :(" in str(feed.html))
        tweet_content = feed.html.find('div', class_='tweet-content').text
        tweet_image_url = feed.html.find('iframe', class_='tweet-video')['src']
        self.assertEqual(tweet_content, 'Testing VIDEO tweets')
        self.assertEqual(tweet_image_url, 'https://www.youtube.com/embed/video-id')
