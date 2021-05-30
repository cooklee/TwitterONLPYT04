from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from twitter_app.models import Tweet
from twitter_app.permission_mixin import MyTestUserPassesTest


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class TweetListView(ListView):
    model = Tweet
    template_name = 'list_view.html'


class CreateTweetView(CreateView):
    model = Tweet
    template_name = 'form.html'
    fields = ['text', 'category']
    success_url = reverse_lazy('tweets')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())


class UpdateTweetView(MyTestUserPassesTest, UpdateView):
    model = Tweet
    template_name = 'form.html'
    fields = ['text']
    success_url = reverse_lazy('tweets')


class DeleteTweetView(MyTestUserPassesTest, DeleteView):
    model = Tweet
    template_name = 'delete.html'
    success_url = reverse_lazy('tweets')
