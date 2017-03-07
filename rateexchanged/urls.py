from django.conf.urls import include, url
from django.contrib import admin
from graparate.views import test, test2, index, login, logout,register, bankpack
from graparate.crawer import DataPipe

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
    url(r'^index/$', index),
    url(r'^$',index),
    url(r'^bank/$', bankpack),
    url(r'^test/$', test),
    url(r'^test2/$', test2),
]
