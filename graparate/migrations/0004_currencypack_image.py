# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0003_auto_20170107_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencypack',
            name='image',
            field=models.ImageField(upload_to='graparate/static/images', blank=True),
        ),
    ]
