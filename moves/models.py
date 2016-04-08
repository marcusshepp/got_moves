from __future__ import unicode_literals

from django.db import models

from main.models import Move


class Classic(Move):
    class Meta:
        ordering = ("-name",)
