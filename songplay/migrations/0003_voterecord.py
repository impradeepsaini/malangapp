# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 10:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songplay', '0002_request_played'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoted', models.BooleanField(default=False)),
                ('downvoted', models.BooleanField(default=False)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songplay.Request')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
