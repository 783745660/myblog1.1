# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-15 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190415_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u8bc4\u8bba\u7528\u6237'),
        ),
    ]
