# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('gender', models.CharField(max_length=20, null=True, choices=[('male', 'Male'), ('female', 'Female')], blank=True)),
                ('city', models.CharField(max_length=250, null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('locale', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
    ]
