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
	date_updated = models.DateTimeField(auto_now=True)


class Likeable(models.Model):
	"""
	Abstract class that gives childern the capability to be `liked`.
	"""
	class Meta:
		abstract = True
	upvotes = models.PositiveIntegerField(null=True, blank=True, default=0)
	downvotes = models.IntegerField(blank=True, null=True, default=0)


class Descriptable(models.Model):
	"""
	Abstract class that gives childern a text description.
	"""
	class Meta:
		abstract = True
	description = models.TextField(blank=True, null=True)


class Video(HasAUser, Likeable, Descriptable, SaveDateCreated):
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
    comments = models.ManyToManyField("Comment")
    placeholder_image = models.FileField(upload_to='uploads/placeholders/')
    credits = models.CharField(max_length=400, null=True, blank=True)
    

class Move(Video):
    """
    Video of a single Cardistry Move.
    Moves should be able to have a sellable tutorial.
    """
    tutorial = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    original = models.BooleanField(default=False)
    category = models.ForeignKey("DefaultCategory")
    estimated_creation_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return "{}".format(self.name)
    
    def price_display(self):
        display = ""
        if self.price is None:
            display += "Free"
        else:
            display = "{}".format(self.price)
        return display
        
    def category_display(self):
        display = ""
        if self.category:
            if self.category.one_handed:
                display += "One Handed: "
            else:
                display += "Two Handed: "
            display += self.category.name
        return display
    
    def date_display(self):
        if self.estimated_creation_date is None:
            return ""
        else: return self.estimated_creation_date
    

class Performance(Video):
    """
    Cardistry Performance Video.
    """
    solo = models.BooleanField(default=True)


DEFAULT_CATEGORY_NAMES = (
    "Fan",
    "Cut",
    "Spread",
    "Ariel",
    "Combination",
    "Spring",
    "Display",
)
class DefaultCategory(SaveDateCreated, Descriptable):
    """
    Type of move.
    """
    name = models.CharField(max_length=50)
    one_handed = models.BooleanField(default=False)
    number_of_packets = models.PositiveIntegerField(null=True, blank=True)


class UserSubmittedCategory(HasAUser, DefaultCategory):
    """
    Type of move.
    """
    class Meta:
        ordering = ("-date_created",)


class Comment(HasAUser, SaveDateCreated):
    """
    Comment on a Video, can comment on a comment.
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
class Rank(SaveDateCreated, Descriptable):
	class Meta:
		ordering = ("-id",)
	name = models.CharField(max_length=100)


class Privilege(SaveDateCreated):
	class Meta:
		pass


class Profile(HasAUser, SaveDateCreated, Descriptable, Likeable):
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
