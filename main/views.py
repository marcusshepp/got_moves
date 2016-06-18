from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods

from rest_framework import generics

from got_moves.settings import LOGIN_REDIRECT_URL as LRU
