# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_form_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='form_type',
            field=models.CharField(choices=[('call', '\u0417\u0430\u043a\u0430\u0437 \u0437\u0432\u043e\u043d\u043a\u0430'), ('write', '\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u043d\u0430\u043c'), ('leasing', '\u041b\u0438\u0437\u0438\u043d\u0433'), ('print', '\u041f\u0435\u0447\u0430\u0442\u044c \u041a\u041f'), ('watch', '\u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u041a\u041f'), ('request', '\u0417\u0430\u043f\u0440\u043e\u0441 \u041a\u041f'), ('to_mail', '\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u043f\u043e\u0447\u0442\u0443 \u041a\u041f'), ('credit-leasing', '\u041a\u0440\u0435\u0434\u0438\u0442-\u041b\u0438\u0437\u0438\u043d\u0433 \u041a\u041f'), ('why-leasing', '\u041f\u043e\u0447\u0435\u043c\u0443 \u043b\u0438\u0437\u0438\u043d\u0433?'), ('why-credit', '\u041f\u043e\u0447\u0435\u043c\u0443 \u043a\u0440\u0435\u0434\u0438\u0442?')], default='write', max_length=32, verbose_name='\u0424\u043e\u0440\u043c\u0430'),
        ),
    ]
