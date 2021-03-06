# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modification date')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('image', django_thumbs.db.models.ImageWithThumbsField(upload_to='core/logo/%Y-%m-%d/')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logos',
            },
        ),
    ]
