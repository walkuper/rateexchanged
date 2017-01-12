# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankPack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('bankname', models.CharField(max_length=100)),
                ('bankcode', models.CharField(max_length=6, blank=True)),
                ('banknameInfo', models.TextField(blank=True)),
                ('bankaddress', models.CharField(max_length=400, blank=True)),
                ('bankphone', models.CharField(max_length=40, blank=True)),
                ('chargefee', models.CharField(max_length=400, blank=True)),
                ('webatm', models.CharField(max_length=1000, blank=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyPack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('currencyname', models.CharField(max_length=50)),
                ('currencyunit', models.CharField(max_length=20)),
                ('currencycode', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('spotbuy', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('spotsell', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('billbuy', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('billsell', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('refreshtime', models.DateTimeField(auto_now=True)),
                ('currencytype', models.ForeignKey(to='graparate.CurrencyPack')),
            ],
        ),
        migrations.CreateModel(
            name='ExATM',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('city', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=600)),
                ('atmaddr', models.CharField(max_length=400)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('bank', models.ForeignKey(to='graparate.BankPack')),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nationname', models.CharField(max_length=50)),
                ('nationInfo', models.TextField(blank=True)),
                ('language', models.CharField(max_length=60)),
                ('languagecode', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='currencypack',
            name='usecountry',
            field=models.ForeignKey(to='graparate.Nation'),
        ),
    ]
