# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20170210_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tractiveunit',
            name='char_abs',
            field=models.CharField(blank=True, choices=[('\u0415\u0441\u0442\u044c', 'Yes'), ('', 'No')], default='', max_length=4, null=True, verbose_name='ABS'),
        ),
        migrations.AlterField(
            model_name='tractiveunit',
            name='char_ebs',
            field=models.CharField(blank=True, choices=[('\u0415\u0441\u0442\u044c', 'Yes'), ('', 'No')], default='', max_length=4, null=True, verbose_name='EBS'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='char_abs',
            field=models.CharField(blank=True, choices=[('\u0415\u0441\u0442\u044c', 'Yes'), ('', 'No')], default='', max_length=4, null=True, verbose_name='ABS'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='char_ebs',
            field=models.CharField(blank=True, choices=[('\u0415\u0441\u0442\u044c', 'Yes'), ('', 'No')], default='', max_length=4, null=True, verbose_name='EBS'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='char_abs',
            field=models.CharField(blank=True, choices=[('\u0415\u0441\u0442\u044c', 'Yes'), ('', 'No')], default='', max_length=4, null=True, verbose_name='ABS'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='char_ebs',
            field=models.CharField(blank=True, choices=[('\u0415\u0441\u0442\u044c', 'Yes'), ('', 'No')], default='', max_length=4, null=True, verbose_name='EBS'),
        ),
    ]
