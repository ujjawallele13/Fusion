# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-05-21 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0013_auto_20200521_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answeraquestion',
            name='total_dislikes',
        ),
        migrations.RemoveField(
            model_name='answeraquestion',
            name='total_likes',
        ),
    ]
