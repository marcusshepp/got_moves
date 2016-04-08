import os
import csv
import random
import requests
from datetime import date
from itertools import chain

from django.core.management.base import BaseCommand
from django.core import serializers
from django.contrib.auth.models import User

from main.models import (
    Category,
)
from main.forms import (
    CategoryForm,
)
from moves.models import (
    Classic,
)
from moves.forms import (
    ClassicForm,
)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('args')
        parser.add_argument('third_arg')

    def handle(self, *args, **options):
        print "Hi, Marcus Shepherd.\nWelcome the Load Data management command."
        arg = "".join([i for i in args])
        if arg == "create":
            print "Creating..."
            third_arg = options.get("third_arg", None)
            if third_arg:
                    user = User.objects.get_or_create(
                        username="qwe",
                        password="qwe"
                    )
                    print user
                    lorem = "http://loripsum.net/api/10/short/headers"
                    request = requests.get(lorem)
                    text = request.text.split("\n")
                    paragraph_tags = [line for line in text if "<p>" in line]
                    num = int(options["third_arg"])
                    LORS = list_of_random_strings
                    # create categories
                    category_names = LORS(paragraph_tags, num)
                    create_categories(category_names, user[0])
                    # create moves
                    create_moves({
                                "name": LORS(paragraph_tags, num),
                                "youtube_link": LORS(paragraph_tags, num),
                                "user": LORS(paragraph_tags, num),
                                "description": LORS(paragraph_tags, num),
                                "placeholder_image": LORS(paragraph_tags, num),
                                "credits": LORS(paragraph_tags, num),
                                "estimated_creation_date": LORS(paragraph_tags, num),
                                "category": [catagory.id for catagory in Category.objects.all()],
                                "user": user,
                                "num":num})
        elif arg == "export":
             print "Exporting..."
             """
             Writes Items + Catagories + Purchases to a file in XML.
             ex: m load_data export <file name>
             """
        #     file_name = options.get("third_arg", None)
        #     if file_name:
        #         if type(file_name) == str: # pointless str test?
        #             path = os.path.join("receipt/data/", file_name)
        #             items = Item.objects.all()
        #             categories = Catagory.objects.all()
        #             purchases = Purchase.objects.all()
        #             # actions = Actions.objects.all()
        #             chained_query = list(chain(items, categories, purchases))
        #             XMLSerializer = serializers.get_serializer("xml")
        #             xml_serializer = XMLSerializer()
        #             with open(path+".xml", 'w') as out:
        #                 xml_serializer.serialize(chained_query, stream=out)
        # elif arg == "import":
        #     print "importing..."
        #     file_name = options.get("third_arg", None)
        #     if file_name:
        #         if type(file_name) == str: # pointless str test?
        #             path = os.path.join("receipt/data/", file_name)
        #             with open(path+".xml", 'r') as out:
        #                 for objec in serializers.deserialize("xml", out):
        #                     objec.save()
        elif arg == "delete":
            print "deleting..."
            # obj = options.get("third_arg", None)
            # if obj == "item":
            #     [i.delete() for i in Item.objects.all()]
            # else:
            #     [i.delete() for i in Purchase.objects.all()]
            #     [i.delete() for i in Catagory.objects.all()]
            #     [i.delete() for i in Item.objects.all()]
            #     [i.delete() for i in Action.objects.all()]
            #     [i.delete() for i in Start.objects.all()]
            #     [i.delete() for i in WhatPage.objects.all()]
            #     [i.delete() for i in User.objects.all()]
        else: print "use args -- `import` or `export`"


def create_moves(kwargs):
    for i in range(kwargs["num"]):
        data = dict()
        item_that_might_already_be_created = Classic.objects.filter(name=kwargs["name"][i])
        if item_that_might_already_be_created.exists() and not str(kwargs["name"][i]).contains("/>"):
            break
        else:
            data["name"] = kwargs["name"][i]
            data["youtube_link"] = kwargs["youtube_link"][i]
            data["user"] = kwargs["user"][0].id
            data["description"] = kwargs["description"][i]
            data["credits"] = kwargs["credits"][i]
            data["estimated_creation_date"] = date.today()
            data["category"] = Category.objects.get(id=1).id
            the_file = open("uploads/300.jpeg", "r")
            data['placeholder_image'] = the_file
            form = ClassicForm(data)
            print form
            if form.is_valid():
                print "valid"
                form.save()
                
def list_of_random_strings(text, num):
    """
    Generates string input for CharField's.
    """
    names = list()
    for i in range(num):
        para_index = random.randrange(1, len(text)-1)
        para_inner_index_left = random.randrange(1, len(text[para_index])-1)
        para_inner_index_right = random.randrange(para_inner_index_left, len(text[para_index])-1)
        before_shortener = text[para_index][para_inner_index_left:para_inner_index_right]
        name = ""
        name += before_shortener
        names.append(name)
    return names

def create_categories(category_names, user):
    for name in category_names:
        d = dict()
        d["name"] = name[:25]
        d["user"] = user.id
        print d
        form = CategoryForm(d)
        print form
        if form.is_valid():
            print "valid"
            form.save()
