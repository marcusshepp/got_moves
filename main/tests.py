import datetime

from django.test import TestCase

from main import models


class MainModelsTest(TestCase):

    def setUp(self):
        pass

    def test_classic_move_and_move_category(self):
        cate_data = {
            "description": "qwe",
            "name": "qwe",
            "one_handed": True,
            "number_of_packets": 3,
        }
        category = models.MoveCategory.objects.create(**cate_data)
        self.assertTrue(models.MoveCategory.objects.filter(name="qwe").exists())
        data = {
            "description": "qwe",
            "name": "qwe",
            "credits": "qwe",
            "estimated_creation_date": datetime.datetime.now(),
            "category": category,
        }
        c = models.ClassicMove.objects.create(**data)
        self.assertTrue(models.ClassicMove.objects.filter(name="qwe").exists())
