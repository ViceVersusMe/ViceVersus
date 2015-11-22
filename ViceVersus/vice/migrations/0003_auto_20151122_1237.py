# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vice', '0002_auto_20151122_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='bounty',
            field=models.ForeignKey(to='vice.Bounty', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='gift_card_value',
            field=models.DecimalField(choices=[('25.00', '$25.00'), ('50', '$50.00'), ('75', '$75.00'), ('100', '$100.00'), ('125', '$125.00'), ('150', '$150.00'), ('175', '$175.00'), ('200', '$200.00'), ('225', '$225.00'), ('250', '$250.00'), ('275', '$275.00'), ('300', '$300.00')], decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='pledge',
            field=models.ForeignKey(to='vice.Pledge', blank=True, null=True),
        ),
    ]
