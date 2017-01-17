# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0007_auto_20170117_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepack',
            name='f',
        ),
        migrations.AddField(
            model_name='currencypack',
            name='image',
            field=models.ImageField(blank=True, upload_to='graparate/static/images/'),
        ),
        migrations.DeleteModel(
            name='ImagePack',
        ),
    ]
