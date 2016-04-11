from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from got_moves.settings import LOGIN_REDIRECT_URL as LRU
from main.models import (
    DefaultCategory,
)
from main.forms import (
    CategoryForm,
)
from main.utils import (
    dict_dot_get,
)
from moves.models import (
    Classic,
)
from moves.forms import (
    ClassicForm,
)

def there_are_classics():
    return Classic.objects.count()

def all_classics():
    return Classic.objects.all()

def there_are_categories():
    return DefaultCategory.objects.count()

def all_categories():
    return DefaultCategory.objects.all()

def handle_classic_post(request):
    data = request.POST.copy()
    print data.items()
    category_name = dict_dot_get(request.POST, "category_name")
    one_handed = data.pop("one_handed") == "1"
    category = DefaultCategory.objects.filter(
        name=category_name, one_handed=one_handed)
    if category:
        data["category"] = category[0].id
    data["user"] = request.user.id
    for k, v in data.items():
        print "after data: ", k, v
    return data

def set_default_catgory_names():
    return list(set([c.name for c in all_categories()]))

@login_required(login_url=LRU)
@require_http_methods(["GET"])
def search_classics_render_template(request):
    """
    Render Search Classics.
    """
    data = dict()
    if there_are_classics(): data["classics"] = all_classics()
    data["category_names"] = set_default_catgory_names()
    print data
    return render(request, "moves/search_classics.html", data)

@login_required(login_url=LRU)
@require_http_methods(["GET"])
def classics_render_form(request):
    """
    Render Classic Form.
    """
    data = dict()
    data["categories"] = all_categories()
    data["category_names"] = set_default_catgory_names()
    return render(request, "moves/add_classic.html", data)

@login_required(login_url=LRU)
@require_http_methods(["POST"])
def post_create_classic(request):
    """
    Post Create New Classic.
    """
    form = ClassicForm(handle_classic_post(request), request.FILES)
    print form
    if form.is_valid():
        print "valid"
        form.save()
    return redirect(reverse_lazy("search_moves"))

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

@require_http_methods(["GET"])
def category_endpoint(request):
    data = dict()
    if there_are_categories():
        data["category_names"] = [ c.name for c in all_categories() ]
        data["category_ids"] = [ c.id for c in all_categories() ]
    print data
    return JsonResponse(data)

@require_http_methods(["GET"])
def delete(request, **kwargs):
    move_id = kwargs["id"]
    Classic.objects.get(id=move_id).delete()
    return redirect(reverse_lazy("search_moves"))
