# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graparate', '0006_auto_20170117_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfs', models.CharField(max_length=10, blank=True)),
                ('image', models.ImageField(upload_to='graparate/static/images/', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='currencypack',
            name='image',
        ),
        migrations.AddField(
            model_name='imagepack',
            name='f',
            field=models.ForeignKey(to='graparate.CurrencyPack', blank=True),
        ),
    ]
