# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-19 18:05
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
            name='ClassicMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('credits', models.CharField(max_length=400, null=True)),
                ('estimated_creation_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassicMovePerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('private', models.BooleanField(default=False)),
                ('youtube_link', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('instagram_link', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('placeholder_image', models.FileField(blank=True, null=True, upload_to='uploads/placeholders/')),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('text', models.TextField()),
                ('comments', models.ManyToManyField(related_name='_comment_comments_+', to='main.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='MoveCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('one_handed', models.BooleanField(default=False)),
                ('number_of_packets', models.PositiveIntegerField(blank=True, null=True)),
                ('user_submitted', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MultiMovePerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('private', models.BooleanField(default=False)),
                ('youtube_link', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('instagram_link', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('placeholder_image', models.FileField(blank=True, null=True, upload_to='uploads/placeholders/')),
                ('classic_moves', models.ManyToManyField(to='main.ClassicMove')),
                ('comments', models.ManyToManyField(to='main.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
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
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rank', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('inspiration', models.TextField()),
                ('url', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-first_name',),
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='UserMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('credits', models.CharField(max_length=400, null=True)),
                ('estimated_creation_date', models.DateField(blank=True, null=True)),
                ('original', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MoveCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserMovePerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('private', models.BooleanField(default=False)),
                ('youtube_link', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('instagram_link', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('placeholder_image', models.FileField(blank=True, null=True, upload_to='uploads/placeholders/')),
                ('comments', models.ManyToManyField(to='main.Comment')),
                ('move', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UserMove')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='multimoveperformance',
            name='user_moves',
            field=models.ManyToManyField(to='main.UserMove'),
        ),
        migrations.AddField(
            model_name='classicmoveperformance',
            name='comments',
            field=models.ManyToManyField(to='main.Comment'),
        ),
        migrations.AddField(
            model_name='classicmoveperformance',
            name='move',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ClassicMove'),
        ),
        migrations.AddField(
            model_name='classicmoveperformance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classicmove',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MoveCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='movecategory',
            unique_together=set([('name', 'one_handed')]),
        ),
    ]
