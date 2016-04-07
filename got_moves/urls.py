from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

from main.views import (
    feed,
    cardist_render_template,
    delete,
    create_profile_render_template,
)

from accounts.views import (
    Login,
    Registeration,
)

urlpatterns = [
    url(r'^foo/', admin.site.urls),
    url(r'^$', feed, name="feed"),
    url(r'^create_profile/$', create_profile_render_template, name="create_profile_template"),
    url(r'^cardist/(?:(?P<username>\w+)/)$', cardist_render_template, name="cardist"),
    url(r'^delete/(?P<id>[0-9]+)/$', delete, name="delete"),

    # account
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^register/$', Registeration.as_view(), name="register"),
]
