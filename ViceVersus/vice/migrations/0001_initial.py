# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('collected', models.BooleanField(default=False)),
                ('busted_picture', models.ImageField(upload_to='')),
                ('collected_by', models.ForeignKey(to='users.UserProfile', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('gift_card_name', models.CharField(max_length=250)),
                ('gift_card_num', models.CharField(max_length=100)),
                ('gift_card_value', models.DecimalField(max_digits=8, choices=[('25', '$25.00'), ('50', '$50.00'), ('75', '$75.00'), ('100', '$100.00'), ('125', '$125.00'), ('150', '$150.00'), ('175', '$175.00'), ('200', '$200.00'), ('225', '$225.00'), ('250', '$250.00'), ('275', '$275.00'), ('300', '$300.00')], decimal_places=2)),
                ('bounty', models.ForeignKey(to='vice.Bounty')),
            ],
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Vice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('strikes', models.IntegerField(null=True, blank=True)),
                ('sponsor', models.ForeignKey(to='users.UserProfile', related_name='sponsor')),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='pledge',
            name='vice',
            field=models.ForeignKey(to='vice.Vice'),
        ),
        migrations.AddField(
            model_name='giftcard',
            name='pledge',
            field=models.ForeignKey(to='vice.Pledge'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='vice',
            field=models.ForeignKey(to='vice.Vice'),
        ),
    ]
