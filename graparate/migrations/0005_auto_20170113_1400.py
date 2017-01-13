# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0004_currencypack_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencypack',
            name='usecountry',
        ),
        migrations.AddField(
            model_name='currencypack',
            name='usecountry',
            field=models.ManyToManyField(to='graparate.Nation'),
        ),
    ]
