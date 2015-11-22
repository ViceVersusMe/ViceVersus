# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151122_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gift_cards',
            field=models.ForeignKey(to='vice.GiftCard', blank=True, null=True),
        ),
    ]
