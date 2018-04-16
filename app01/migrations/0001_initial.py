# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=300, blank=True, null=True)),
                ('hire_date', models.DateField(auto_now_add=True)),
                ('department', models.ForeignKey(to='app01.Department')),
            ],
        ),
    ]
