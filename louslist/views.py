from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

import urllib, json



class IndexView(generic.ListView):
    template_name = 'louslist/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        url = "http://luthers-list.herokuapp.com/api/deptlist/?format=json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        context= {
            'data' : data,
        }

        return context

    def get_queryset(self):
        return ''


class LoginView(generic.ListView):
    template_name = 'louslist/login.html'

    def get_queryset(self):
        return ''

