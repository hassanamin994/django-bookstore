# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bs_app', '0005_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(default='image', upload_to='router_specifications'),
        ),
    ]
