# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0003_auto_20180413_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='q1',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q2',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q3',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='q4',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='result',
            field=models.CharField(default='Golden Retriever', max_length=20),
        ),
    ]
