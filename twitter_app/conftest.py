import pytest
from django.contrib.auth.models import User

from twitter_app.models import Tweet, Category


@pytest.fixture
def user():
    u = User()
    u.username = "cooklee"
    u.save()
    return u

@pytest.fixture
def categories():
    cats = []
    for x in range(4):
        cats.append(Category.objects.create(name=f'{x}'))
    return cats

@pytest.fixture
def category():
    c = Category.objects.create(name=f'123')
    return c

@pytest.fixture
def tweet(user):
    t = Tweet()
    t.text = "ala ma kota"
    t.owner = user
    t.save()
    return t


@pytest.fixture
def tweets_10(user):
    lst = []
    for _ in range(10):
        t = Tweet()
        t.text = "ala ma kota"
        t.owner = user
        t.save()
        lst.append(t)
    return lst