# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bs_app', '0017_auto_20170430_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='published_at',
            field=models.DateField(null=True),
        ),
    ]
