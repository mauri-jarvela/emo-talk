# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 02:49
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default=b'', null=True, upload_to=api.models.upload_to),
        ),
    ]