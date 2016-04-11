from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login

from main.views import (
    feed,
    cardist_render_template,
    delete,
    create_profile_render_template,
)
from moves.views import (
    search_classics_render_template,
    categories_render_form,
    post_create_category,
    classics_render_form,
    post_create_classic,
    category_endpoint,
)
from accounts.views import (
    Login,
    Registeration,
)

urlpatterns = patterns("",
    url(r'^foo/', admin.site.urls),
    url(r'^$', feed, name="feed"),
    url(r'^create_profile/$', create_profile_render_template, name="create_profile_template"),
    url(r'^cardist/(?:(?P<username>\w+)/)$', cardist_render_template, name="cardist"),
    url(r'^delete/(?P<id>[0-9]+)/$', delete, name="delete"),

    # moves
    url(r'^moves/$', search_classics_render_template, name="search_moves"),
    url(r'^moves/add$', classics_render_form, name="classic_form"),
    url(r'^moves/adding$', post_create_classic, name="post_classic_move"),
    url(r'^moves/delete/(?P<id>[0-9]+)/$', delete, name="delete_classic"),

    # categories
    url(r'^categories/$', categories_render_form, name="categories"),
    url(r'^create_category/$', post_create_category, name="create_category"),
    url(r'^api/categories/$', category_endpoint, name="api_categories"),

    # account
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^register/$', Registeration.as_view(), name="register"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
