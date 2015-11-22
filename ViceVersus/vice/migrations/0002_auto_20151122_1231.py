# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='busted_picture',
            field=models.ImageField(upload_to='', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='collected_by',
            field=models.ForeignKey(to='users.UserProfile', blank=True, null=True),
        ),
    ]
