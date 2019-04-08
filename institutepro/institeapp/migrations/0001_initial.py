# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-08 07:47
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('courses', multiselectfield.db.fields.MultiSelectField(choices=[('python', 'python'), ('django', 'Django'), ('api', 'API'), ('ui', 'UI'), ('flask', 'FLASK')], max_length=200)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('hyd', 'Hyderabad'), ('bang', 'Bangalore'), ('che', 'Chennai')], max_length=200)),
                ('shift', multiselectfield.db.fields.MultiSelectField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('night', 'Night')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('date', models.DateField()),
                ('feedback', models.TextField(max_length=300)),
            ],
        ),
    ]
