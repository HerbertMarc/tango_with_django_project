# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-02 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
