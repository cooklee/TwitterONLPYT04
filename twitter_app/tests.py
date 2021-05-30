import pytest
from django.test import Client

# Create your tests here.
from django.urls import reverse

from twitter_app.models import Tweet


@pytest.mark.django_db
def test_ala_ma_kota(tweet):
    c = Client()
    response = c.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_all_tweets(tweets_10):
    c = Client()
    response = c.get(reverse('tweets'))
    assert response.status_code == 200
    assert len(response.context['object_list']) == len(tweets_10)
    for item in response.context['object_list']:
        assert item in tweets_10


@pytest.mark.django_db
def test_get_update_tweet(tweet):
    c = Client()
    c.force_login(tweet.owner)
    update_url = reverse('update_tweets', args=(tweet.id,))
    response = c.get(update_url)
    assert response.status_code == 200
    assert response.context['object'] == tweet


@pytest.mark.django_db
def test_get_update_tweet_not_login(tweet):
    c = Client()
    response = c.get(reverse('update_tweets', args=(tweet.id,)))
    assert response.status_code == 302
    login_url = reverse('login')
    assert response.url.startswith(login_url)


@pytest.mark.django_db
def test_create_tweet(user, categories):
    c = Client()
    c.force_login(user)
    data = {'text': 'ala ma kota', 'category':categories[0].pk}
    url = reverse('create_tweets')
    response = c.post(url, data)
    t = Tweet.objects.first()
    assert response.status_code == 302
    assert t.text == data['text']
    assert t.category == categories[0]
