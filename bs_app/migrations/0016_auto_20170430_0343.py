# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 03:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bs_app', '0015_auto_20170430_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='book_id',
            new_name='book',
        ),
    ]
