# -*- coding: utf8 -*-
from datetime import datetime
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from rateexchanged import settings
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from bs4 import BeautifulSoup as bs
import urllib.request, requests, sys, json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
#from urllib2 import urlopen, HTTPError, request
from graparate.crawer import DataPipe

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
    currencyurl = u'http://127.0.0.1:8000/static/java/currency_type.json'
    url = u'https://tw.rter.info/capi.php'
    jsonparser1 = requests.get(currencyurl).json()
    jsonparser2 = requests.get(url).json()
    print(jsonparser1)
    #新增複數幣別取值
    txt=json.loads(DataPipe("AUD"))
    return render(request,'index.html',{'data':txt, 'ctype':jsonparser1, 'yrate':jsonparser2})

    #return render_to_response('index.html',locals())

def bankpack(request):
    currencyurl = u'http://127.0.0.1:8000/static/java/currency_type.json'
    url = u'https://tw.rter.info/capi.php'
    #txt=json.loads(url)
    jsonparser1 = requests.get(url).json()
    jsonparser2 = requests.get(url).json()
    print (type(jsonparser))
    #getdata = jsonparser.read()
    #pos_start = getdata.find('[')
    #pos_end = getdata.find(']')
    #usedata = getdata[(pos_start):pos_end]
    #getjson = json.loads(usedata)
    #for i in range(len(getjson)):
    #    print (getjson[i]['Exrate'])
    return render(request,'index.html',{'yrate':jsonparser})

def test(request):
    rArr=[]
    r = requests.get(u"http://127.0.0.1:8000/static/java/currency_type.json").json()
    print (type(r))
    rArr.append(r)
    rr = json.dumps(rArr)
    print ('rr type :' + str(type(rr)))
    print ('rr len:' + str(len(rr)))
    rrr = json.loads(rr)
    print ('rrr type :' + str(type(rrr)))
    print ('rrr len :' + str(len(rrr)))
    return render(request, 'test.html', {
           'r': rrr,
           })
    #return render_to_response('test.html',locals())


def test2(request):
    return render_to_response('test2.html',locals())

base_dir = settings.BASEDIR()
filter = base_dir + "/templates/" + ""
