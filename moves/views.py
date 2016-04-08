from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from got_moves.settings import LOGIN_REDIRECT_URL as LRU
from main.models import (
    Category,
)
from main.forms import (
    CategoryForm,
)
from .models import Classic
from .forms import ClassicForm

def there_are_classics():
    return Classic.objects.count()

def all_classics():
    return Classic.objects.all()

def there_are_categories():
    return Category.objects.count()

def all_categories():
    return Category.objects.all()

@login_required(login_url=LRU)
@require_http_methods(["GET"])
def classics_render_template(request):
    """
    """
    data = dict()
    if there_are_classics(): data["classics"] = all_classics()
    return render(request, "moves/classics.html", data)

@login_required(login_url=LRU)
@require_http_methods(["GET"])
def categories_render_form(request):
    """
    """
    data = dict()
    if there_are_categories(): data["categories"] = all_categories()
    return render(request, "moves/categories.html", data)

@login_required(login_url=LRU)
@require_http_methods(["POST"])
def post_create_category(request):
    """
    """
    data = dict()
    print request.POST
    form = CategoryForm(request.POST)
    print form
    if form.is_valid():
        print "valid"
        form.save()
    data["categories"] = all_categories()
    return render(request, "moves/categories.html", data)
