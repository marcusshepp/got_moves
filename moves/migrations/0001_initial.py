# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from main.models import DEFAULT_CATEGORY_NAMES
from main.forms import DefaultCategoryForm

class Migration(migrations.Migration):
    def foo(apps, schema_editor):
        # FooBar = apps.get_model("main", "DefaultCategory")
        for name in DEFAULT_CATEGORY_NAMES:
            for i in range(2):
                data = dict()
                data["name"] = name
                data["one_handed"] = i == 1
                form = DefaultCategoryForm(data)
                print form
                if form.is_valid():
                    print "val"
                    form.save()

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classic',
            fields=[
                ('move_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Move')),
            ],
            options={
                'ordering': ('-name',),
            },
            bases=('main.move',),
        ),
        migrations.RunPython(foo),
    ]
