from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader



class IndexView(generic.ListView):
    template_name = 'louslist/index.html'

    def get_queryset(self):
        return ''


class LoginView(generic.ListView):
    template_name = 'louslist/login.html'

    def get_queryset(self):
        return ''




def index(request):
    template = loader.get_template('louslist/index.html')
    context = {
        'latest_question_list': ''
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
