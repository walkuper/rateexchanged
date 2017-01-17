# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0005_auto_20170113_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankpack',
            name='webatm',
            field=models.URLField(blank=True),
        ),
        migrations.RemoveField(
            model_name='currencypack',
            name='bankpub',
        ),
        migrations.AddField(
            model_name='currencypack',
            name='bankpub',
            field=models.ManyToManyField(blank=True, to='graparate.BankPack'),
        ),
    ]
