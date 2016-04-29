# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20160411_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='push_friend_req',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='push_liked_msg',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='push_new_msg',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='push_read_msg',
            field=models.BooleanField(default=True),
        ),
    ]
