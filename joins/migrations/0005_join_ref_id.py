# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20160626_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='ABC', max_length=120),
        ),
    ]
