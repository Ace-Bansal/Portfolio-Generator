# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20170627_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_done',
            field=models.BooleanField(default=False),
        ),
    ]