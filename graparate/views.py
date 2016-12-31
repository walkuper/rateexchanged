from datetime import datetime
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from rateexchanged import settings
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from bs4 import BeautifulSoup as bs
import requests
import sys
import json


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())

def index(request):
    return render_to_response('index.html',locals())



base_dir = settings.BASEDIR()
filter = base_dir + "/templates/" + ""
