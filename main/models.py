from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class HasAUser(models.Model):
    class Meta:
        abstract = True
        ordering = ["-id"]
    user = models.ForeignKey(User)


class Move(HasAUser):
    name = models.CharField(max_length=50, blank=False, null=False)
    youtube_link = models.CharField(max_length=1000, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    comments = models.ManyToManyField("Comment")
    def __unicode__(self):
        return "{}".format(self.name)


class Comment(HasAUser):
    text = models.TextField()
    likes = models.IntegerField(null=True, blank=True)