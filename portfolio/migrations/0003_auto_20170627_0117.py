# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170627_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='phone_number',
            field=models.BigIntegerField(default=12345678),
        ),
    ]