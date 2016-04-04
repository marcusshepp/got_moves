from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import (
    MoveForm,
    CommentForm,
)
from .models import (
    Move,
    Comment,
)

# foobarpop
LOGIN_REDIRECT = '/login/'

def dict_dot_get(dictionary, key):
    return dictionary.get(key, None)

def username_exists(username):
    # does `username` exist?
    return User.objects.filter(
        username=username).count() > 0

def user_by_username(username):
    # return `user` for this username
    return User.objects.get(username=username)

def there_are_moves():
    # True if there are moves else False
    return Move.objects.all().count() > 0

def has_moves(user):
    # does this User have any moves?
    return Move.objects.filter(
        user_id=user.id).count() > 0

def all_private_moves():
    # Returns all private moves
    return Move.objects.filter(private=False)

def moves_for(user):
    # Returns all moves for `user`.
    return Move.objects.filter(user_id=user.id)

def create_object(ModelForm, data):
    form = ModelForm(data)
    if form.is_valid():
        form.save()
        val = True
    else: val = False
    return val

def create_move(move_form_data):
    create_object(MoveForm, move_form_data)

def page_data_cardist(request, kwargs):
    data = dict()
    request_dot_get_username = dict_dot_get(kwargs, "username")
    # is the request user the owner of this profile?
    data["owner_viewing"] = request.user.username == request_dot_get_username
    data["move_form"] = MoveForm
    data["moves"] = moves_for(request.user)
    return data

@login_required(login_url=LOGIN_REDIRECT)
def feed(request):
    data = dict()
    if there_are_moves():
        data["moves"] = all_private_moves()
    else:
        data["no_moves"] = True
    return render(request, "main/feed.html", data)


@login_required(login_url=LOGIN_REDIRECT)
def cardist_render_template(request, *args, **kwargs):
    """
    Cardist's profile
    `/cardist/sheph2mj`
    url required kwargs: username

    NOTE:
        should try to restrict request method to `get`.
    """
    data = dict()
    request_dot_get_username = dict_dot_get(kwargs, "username")
    if request_dot_get_username:
        if username_exists(request_dot_get_username):
            data = page_data_cardist(request, kwargs)
    else:
        # no username
        data["no_username"] = True
    return render(request, "main/cardist.html", data)

@login_required(login_url=LOGIN_REDIRECT)
def post_create_move_renders_profile(request, *args, **kwargs):
    """
    Creates a new `Move`.

    NOTE:
        should try to restrict request method to `POST`.
    """
    data = dict()
    request_dot_get_username = dict_dot_get(request, "username")
    if request_dot_get_username:
        # foo bar
        if username_exists(request_dot_get_username):
            move_form_data = dict()
            move_form_data["name"] = dict_dot_get(request.POST, "name")
            move_form_data["youtube_link"] = dict_dot_get(request.POST, "youtube_link")
            tutorial = dict_dot_get(request.POST, "tutorial")
            if tutorial: move_form_data["tutorial"] = True
            else: move_form_data["tutorial"] = False
            private = dict_dot_get(request.POST, "private")
            if private: move_form_data["private"] = True
            else: move_form_data["private"] = False
            move_form_data["user"] = request.user.id
            create_move(move_form_data)
    else:
        # no username
        data["no_username"] = True
    return render(request, "main/cardist.html", data)

def delete(request, *args, **kwargs):
    data = dict()
    move_id = kwargs["id"]
    Move.objects.get(id=move_id).delete()
    data["moves"] = Move.objects.all()
    return redirect("/")
