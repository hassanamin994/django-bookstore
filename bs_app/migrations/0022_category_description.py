# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bs_app', '0021_author_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]