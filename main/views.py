from django.shortcuts import render, redirect

from .forms import (
    MoveForm,
    CommentForm,
)
from .models import (
    Move,
    Comment,
)


def foo(request):
    data = dict()
    if request.method == "GET":
        data["move_form"] = MoveForm
    else:
        move_form_data = dict()
        move_form_data["name"] = request.POST.get("name", None)
        move_form_data["youtube_link"] = request.POST.get("youtube_link", None)
        move_form_data["user"] = request.user.id
        move_form = MoveForm(move_form_data)
        if move_form.is_valid():
            move_form.save()
    data["moves"] = Move.objects.all()
    print data["moves"]
    return render(request, "base.html", data)
    
def delete(request, *args, **kwargs):
    data = dict()
    move_id = kwargs["id"]
    print move_id
    Move.objects.get(id=move_id).delete()
    data["moves"] = Move.objects.all()
    return redirect("/")