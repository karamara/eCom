# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('productName', models.TextField(max_length=255)),
                ('brand', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('created_at', models.DateField()),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
