# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencypack',
            name='bankpub',
            field=models.ForeignKey(default=datetime.datetime(2017, 1, 6, 23, 10, 2, 259384, tzinfo=utc), to='graparate.BankPack'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankpack',
            name='webatm',
            field=models.URLField(),
        ),
        migrations.RemoveField(
            model_name='currencypack',
            name='usecountry',
        ),
        migrations.AddField(
            model_name='currencypack',
            name='usecountry',
            field=models.ManyToManyField(to='graparate.Nation'),
        ),
        migrations.RemoveField(
            model_name='currencyrate',
            name='currencytype',
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='currencytype',
            field=models.ManyToManyField(to='graparate.CurrencyPack'),
        ),
    ]
