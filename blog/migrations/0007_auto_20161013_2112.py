# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20161013_2111'),
        ('blog', '0006_auto_20161012_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPagePerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='common.Person')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.AddField(
            model_name='blogpageperson',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='blog.BlogPage'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_authors',
            field=models.ManyToManyField(blank=True, through='blog.BlogPagePerson', to='common.Person'),
        ),
    ]