# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0002_auto_20170106_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencypack',
            name='usecountry',
        ),
        migrations.AddField(
            model_name='currencypack',
            name='usecountry',
            field=models.ForeignKey(default=django.utils.timezone.now, to='graparate.Nation'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='currencyrate',
            name='currencytype',
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='currencytype',
            field=models.ForeignKey(default=django.utils.timezone.now, to='graparate.CurrencyPack'),
            preserve_default=False,
        ),
    ]
