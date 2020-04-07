# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-07 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('category', models.CharField(choices=[('Education', 'Education'), ('Housing', 'Housing'), ('Health', 'Health')], max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]