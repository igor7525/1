# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20170319_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='catalog.Products', verbose_name='photo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prop',
            name='propitem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.PropItem', verbose_name='characteristic'),
            preserve_default=False,
        ),
    ]
