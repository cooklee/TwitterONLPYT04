
from django.contrib import admin
from django.urls import path
from twitter_app import views


urlpatterns = [
    path("all/", views.TweetListView.as_view(), name='tweets'),
    path("create/", views.CreateTweetView.as_view(), name='create_tweets'),
    path("delete/<int:pk>/", views.DeleteTweetView.as_view(), name='delete_tweets'),
    path("update/<int:pk>/", views.UpdateTweetView.as_view(), name='update_tweets'),
]
