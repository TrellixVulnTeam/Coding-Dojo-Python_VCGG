# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-17 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fav_book_app', '0002_book_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users_who_like',
        ),
    ]
