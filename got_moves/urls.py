"""got_moves URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

from main.views import (
    feed,
    cardist,
    delete,
)

from accounts.views import (
    Login,
    Registeration,
)

urlpatterns = [
    url(r'^foo/', admin.site.urls),
    url(r'^$', feed, name="feed"),
    url(r'^cardist/(?:(?P<username>\w+)/)$', cardist, name="cardist"),
    url(r'^delete/(?P<id>[0-9]+)/$', delete, name="delete"),

    # account
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^register/$', Registeration.as_view(), name="register"),
]
