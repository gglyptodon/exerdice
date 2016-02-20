# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exerdice_core', '0002_die_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_dice', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExerciseTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('datetime_performed', models.DateTimeField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exerdice_core.ExerciseDefinition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='die',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='exercisedefinition',
            name='assoc_dice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exerdice_core.Die'),
        ),
    ]
