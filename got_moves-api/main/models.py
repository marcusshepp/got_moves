from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


DEFAULT_CATEGORY_NAMES = (
    "Fan",
    "Cut",
    "Spread",
    "Ariel",
    "Combination",
    "Spring",
    "Display",
)
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


class HasAUser(models.Model):
    """
    Abstract class used to populate childern with a `user` field
    """
    class Meta:
        abstract, ordering = True, ("-id",)
    user = models.ForeignKey(User)


class DateCreatedAndUpdate(models.Model):
    """
    Abstract class used to populate childern with a `date_created` field
    """
    class Meta:
        abstract, ordering = True, ("-id",)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def time_past_since_creation(self):
        time = (timezone.now()-self.date_created)
        hours = time.seconds / 60 / 60
        weeks = time.days / 7
        return "Weeks: {weeks}, Days: {days}, Hours: {hours}, Seconds: {seconds}".format(
            days=time.days, seconds=time.seconds, weeks=weeks, hours=hours
        )


class Likeable(models.Model):
    """
    Abstract class that gives childern the capability to be `liked`.
    """
    class Meta:
        abstract = True
    likes = models.IntegerField(null=True, blank=True, default=0)


class Descriptable(models.Model):
    """
    Abstract class that gives childern a text description.
    """
    class Meta:
        abstract = True
    description = models.TextField(blank=True, null=True)


class Named(models.Model):
    """
    Abstract class used to populate children with a name.
    """
    class Meta:
        abstract = True
    name = models.CharField(max_length=250, null=False)


class UniquelyNamed(models.Model):
    """
    Abstract class used to populate children with a unique name.
    """
    class Meta:
        abstract = True
    name = models.CharField(max_length=250, null=False)

    def __str__(self):
        return "{}".format(self.name)


class MoveCategory(UniquelyNamed, DateCreatedAndUpdate, Descriptable):
    """
    Type of move.
    """
    class Meta:
        unique_together = ("name", "one_handed",)
        ordering = ("name",)
    one_handed = models.BooleanField(default=False)
    number_of_packets = models.PositiveIntegerField(null=True, blank=True)
    user_submitted = models.ForeignKey(User, null=True)

    def __str__(self):
        display = ""
        if self.name:
            if self.one_handed:
                display += "One Handed "
            else:
                display += "Two Handed "
            display += self.name
        return "{}".format(display)

    def display(self):
        return self.__str__()

    def detail_url(self):
        return "/move_category/{0}".format(self.id)


class Move(UniquelyNamed, Descriptable, DateCreatedAndUpdate, Likeable):
    """
    The parent class of ClassicMove and UserMove.
    """
    class Meta:
        abstract = True
    credits = models.CharField(max_length=400, null=True)
    category = models.ForeignKey("MoveCategory")
    estimated_creation_date = models.DateField(blank=True, null=True)
    # TODO: switch back after adding Users in.
    # submitted_by = models.ForeignKey(User)

    def date_display(self):
        if self.estimated_creation_date is None:
            return ""
        else: return self.estimated_creation_date

    def category_detail_url(self):
        return self.category.detail_url()

    def category_display(self):
        return self.category.display()


class ClassicMove(Move):
    """
    This is a Classic Cardistry move that is practiced by many
    cardists around the world. It is noted as being ground
    breaking and having a heavy influence on the art as a whole.
    """
    pass


class UserMove(Move):
    """
    User submitted Move. Original Moves will show up on the Cardists
    profile.
    """
    # users can submit moves that were created by other Cardists.
    original = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}".format(self.name)


class Video(Named, HasAUser, Likeable, Descriptable, DateCreatedAndUpdate):
    """
    Parent Class of SingleMovePerformance and MultiMovePerformance.
    """
    class Meta:
        abstract, ordering = True, ("-id",)
    private = models.BooleanField(default=False)
    youtube_link = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    instagram_link = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    comments = models.ManyToManyField("Comment")
    placeholder_image = models.FileField(upload_to='uploads/placeholders/',
        null=True, blank=True)


class ClassicMovePerformance(Video):
    """
    Cardistry Performance Video of a single ClassicMove.
    """
    move = models.ForeignKey("ClassicMove", null=True)


class UserMovePerformance(Video):
    """
    Cardistry Performance Video of a single User Defined Move.
    """
    move = models.ForeignKey("UserMove", null=True) # should these move fields be null????


class MultiMovePerformance(Video):
    """
    Cardistry Video of (multiple) performances of multiple Moves.
    """
    user_moves = models.ManyToManyField("UserMove")
    classic_moves = models.ManyToManyField("ClassicMove")


class Comment(Likeable, HasAUser, DateCreatedAndUpdate):
    """
    Comment on a Video, can comment on a comment.
    """
    class Meta:
        ordering = ("-date_created",)
    text = models.TextField()
    comments = models.ManyToManyField("self")


class Rank(Named, DateCreatedAndUpdate, Descriptable):
    class Meta:
        ordering = ("-id",)


class Privilege(DateCreatedAndUpdate):
    pass


class Profile(HasAUser, DateCreatedAndUpdate, Descriptable, Likeable):
    """
    Cardist's Profile
    """
    class Meta:
        ordering = ("-first_name",)
    rank = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # I want this to be comma seperated names
    # that potentially link to other cardist's
    # profiles if they exist.
    inspiration = models.TextField()
    url = models.CharField(max_length=500)
    # not sure how to implement fav classic move
    # maybe foreign key to classicmove model
    # maybe just a charfield
    # favorite_classic_move = models.
