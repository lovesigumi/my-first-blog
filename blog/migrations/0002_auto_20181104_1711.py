# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-04 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
    ]