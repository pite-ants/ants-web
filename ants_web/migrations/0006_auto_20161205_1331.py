# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-05 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ants_web', '0005_location_capacity'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='term',
            name='kind',
            field=models.CharField(max_length=32),
        ),
    ]