# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('urlhash', models.TextField(blank=True, default=b'', null=True, verbose_name='urlhash')),
                ('useragent', models.TextField(blank=True, default=b'', null=True, verbose_name='useragent')),
                ('name', models.CharField(max_length=32, verbose_name='first name')),
                ('phone', models.CharField(max_length=32, verbose_name='phone')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='subject')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('text', models.TextField(blank=True, null=True, verbose_name='text')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site')),
            ],
        ),
    ]