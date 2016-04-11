# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.4 on 2016-04-10 16:36
=======
# Generated by Django 1.9.5 on 2016-04-08 20:51
>>>>>>> 2099efa10d05f965deccd0aa51665afdb92a03de
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('comments', models.ManyToManyField(related_name='_comment_comments_+', to='main.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='DefaultCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('one_handed', models.BooleanField(default=False)),
                ('number_of_packets', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('youtube_link', models.CharField(blank=True, max_length=1000, unique=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('placeholder_image', models.FileField(upload_to='uploads/placeholders/')),
                ('credits', models.CharField(max_length=400, blank=True, null=True)),
                ('tutorial', models.BooleanField(default=False)),
                ('for_sale', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('original', models.BooleanField(default=False)),
                ('estimated_creation_date', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DefaultCategory')),
                ('comments', models.ManyToManyField(to='main.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('youtube_link', models.CharField(blank=True, max_length=1000, unique=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
<<<<<<< HEAD
                ('placeholder_image', models.FileField(upload_to='uploads/placeholders/')),
                ('credits', models.CharField(max_length=400, blank=True, null=True)),
=======
                ('placeholder_image', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('credits', models.CharField(max_length=400)),
>>>>>>> 2099efa10d05f965deccd0aa51665afdb92a03de
                ('solo', models.BooleanField(default=True)),
                ('comments', models.ManyToManyField(to='main.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('rank', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('inspiration', models.TextField()),
                ('url', models.CharField(max_length=500)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-first_name',),
            },
        ),
        migrations.CreateModel(
            name='UserSubmittedCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('one_handed', models.BooleanField(default=False)),
                ('number_of_packets', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
