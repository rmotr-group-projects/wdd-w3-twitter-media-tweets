from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.http.response import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout as django_logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .models import Tweet, ImageTweet, VideoTweet
from .forms import TweetForm

User = get_user_model()


@login_required()
def logout(request):
    django_logout(request)
    return redirect('/')


def home(request, username=None):
    if not request.user.is_authenticated():
        if not username or request.method != 'GET':
            return redirect(settings.LOGIN_URL + '?next=%s' % request.path)

    user = request.user

    if request.method == 'POST':
        form = TweetForm(request.POST)
        # for k, v in form.data.items():
        #     print(str(v))
        # print(form.is_valid())
        if form.is_valid():
            tweet = Tweet.objects.create(user=user, content=form.cleaned_data['content'])
            if form.cleaned_data['image_url']:
                tweet.media = ImageTweet.objects.create(image_url=form.cleaned_data['image_url'])
            elif form.cleaned_data['video_url']:
                tweet.media = VideoTweet.objects.create(video_url=form.cleaned_data['video_url'])
            tweet.save()
            # print(tweet.media)
            # print(str(form))
            # print(str(form.cleaned_data))
        # raise NotImplementedError()
        # pass

    form = TweetForm()

    if username:
        user = get_object_or_404(get_user_model(), username=username)
        form = None

    tweets = Tweet.objects.filter(user=user)
    return render(request, 'feed.html', {
        'form': form,
        'twitter_profile': user,
        'tweets': tweets
    })


@login_required()
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if tweet.user != request.user:
        raise PermissionDenied
    tweet.delete()
    messages.success(request, 'Tweet successfully deleted')
    return redirect(request.GET.get('next', '/'))
