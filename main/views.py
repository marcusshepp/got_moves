from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import (
    MoveForm,
    CommentForm,
)
from .models import (
    Move,
    Comment,
)

def feed(request):
    if request.user.is_anonymous():
        return redirect("/login/")
    data = dict()
    data["moves"] = Move.objects.filter(private=False)
    for move in data["moves"]:
        print move.tutorial
    return render(request, "main/feed.html", data)

def profile(request, *args, **kwargs):
    if request.user.is_anonymous():
        return redirect("/login/")
    data = dict()
    username = kwargs.get("username", None)
    user_who_owns_account = User.objects.get(username=username)
    data["user_who_owns_account"] = user_who_owns_account
    data["owner_viewing"] = request.user.username == username
    if request.method == "GET":
        data["move_form"] = MoveForm
    else:
        move_form_data = dict()
        move_form_data["name"] = request.POST.get("name", None)
        move_form_data["youtube_link"] = request.POST.get("youtube_link", None)
        tutorial = request.POST.get("tutorial", None)
        if tutorial: move_form_data["tutorial"] = True
        else: move_form_data["tutorial"] = False
        private = request.POST.get("private", None)
        if private: move_form_data["private"] = True
        else: move_form_data["private"] = False
        move_form_data["user"] = request.user.id
        move_form = MoveForm(move_form_data)
        if move_form.is_valid():
            move_form.save()
    if data["owner_viewing"]:
        data["moves"] = Move.objects.filter(user=user_who_owns_account.id)
    else: data["moves"] = Move.objects.filter(user=user_who_owns_account.id, private=False)
    print data["moves"]
    return render(request, "main/account.html", data)
    
def delete(request, *args, **kwargs):
    data = dict()
    move_id = kwargs["id"]
    Move.objects.get(id=move_id).delete()
    data["moves"] = Move.objects.all()
    return redirect("/")