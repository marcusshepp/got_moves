from django.contrib import admin

from .models import (
    Move,
    Comment,
)

admin.site.register(Move)
admin.site.register(Comment)