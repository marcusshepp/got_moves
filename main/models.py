from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class HasAUser(models.Model):
    """
    Abstract class used to populate childern with a `user` field
    """
    class Meta:
        abstract, ordering = True, ("-id",)
    user = models.ForeignKey(User)


class SaveDateCreated(models.Model):
    """
    Abstract class used to populate childern with a `date_created` field
    """
    class Meta:
        abstract, ordering = True, ("-id",)
    date_created = models.DateTimeField(auto_now_add=True)


class Video(HasAUser, SaveDateCreated):
    """
    Parent Class of `Move` and `Performance`.
    """
    class Meta:
        abstract, ordering = True, ("-id",)
    name = models.CharField(
        max_length=50, blank=False, null=False)
    private = models.BooleanField(default=False)
    youtube_link = models.CharField(
        max_length=1000, blank=True, unique=True)
    rating = models.IntegerField(
        null=True, blank=True)
    comments = models.ManyToManyField("Comment")
    description = models.TextField(null=True, blank=True)
    placeholder_image = models.FileField(upload_to='uploads/')
    credits = models.CharField(max_length=400)


class Move(Video):
    """
    Video of a single Cardistry Move.
    Moves should be able to have a sellable tutorial.
    Performance videos should be seperate from moves.
    """
    tutorial = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    original = models.BooleanField(default=False)
    category = models.ForeignKey("Category")
    estimated_creation_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return "{}".format(self.name)


class Performance(Video):
    """
    Cardistry Performance Video.
    """
    solo = models.BooleanField(default=True)


CATEGORY_NAMES = (
    "Fan",
    "Cut",
    "Spread",
    "Ariel",
    "Combination",
    "Spring",
    "Display",
)
class Category(HasAUser, SaveDateCreated):
    """
    Type of move.
    """
    class Meta:
        ordering = ("-date_created",)
    name = models.CharField(max_length=50)
    one_handed = models.BooleanField(default=False)
    number_of_packets = models.PositiveIntegerField(null=True, blank=True)


class Comment(HasAUser, SaveDateCreated):
    """
    Commnet on a Video, can comment on a comment.
    """
    class Meta:
        ordering = ("-date_created",)
    text = models.TextField()
    likes = models.IntegerField(null=True, blank=True)
    comments = models.ManyToManyField("self")


RANK_TITLES = (
    "Ensign",
    "Lieutenant Junior Grade",
    "Lieutenant",
    "Captain",
    "Major",
    "Lieutenant Colonel",
    "Colonel",
    "Commander",
    "Rear Admiral",
    "Vice Admiral",
    "Admiral",
)
"""
Admiral - (Theoretical - non-canon.)
Vice Admiral - (Theoretical - non-canon.)
Rear Admiral - (Only Flag Rank that appears in series canon.)
Commander - Equivalent to a Commodore, Commanding Officer of a Battlestar Group.
Colonel
Lieutenant Colonel (Jack Fisk "Razor")
Major
Captain
Lieutenant
Lieutenant Junior Grade
Ensign
-------
"Bronze",
"Silver",
"Gold",
"Platinum",
"Diamond",
"Master",
"Challenger",
"Virt",
"""
class Profile(HasAUser, SaveDateCreated):
    """
    Ideas for how to rank up:
        - number of comments
        - number of comment upvotes
        - number of comments on users videos
    """
    class Meta:
        ordering = ("-first_name",)
    rank = models.CharField(max_length=50)
    description = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    inspiration = models.TextField()
    url = models.CharField(max_length=500)
    likes = models.IntegerField(
        null=True, blank=True)
