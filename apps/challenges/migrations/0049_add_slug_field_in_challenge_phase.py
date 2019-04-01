# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-31 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0048_add_fields_to_store_host_aws_keys")]

    operations = [
        migrations.AddField(
            model_name="challengephase",
            name="slug",
            field=models.SlugField(max_length=200, null=True, unique=True),
        )
    ]