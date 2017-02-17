# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 20:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('private', models.BooleanField(default=False)),
                ('field_type', models.CharField(choices=[('s', 'Single-line text'), ('m', 'Multi-line text'), ('i', 'Integer'), ('f', 'Float')], default='s', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s', models.CharField(blank=True, default='', max_length=100)),
                ('m', models.TextField(blank=True, default='', max_length=500)),
                ('i', models.IntegerField(blank=True, default=0)),
                ('f', models.FloatField(blank=True, default=0.0)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='api.CustomField', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('model_no', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='KipventoryUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netid', models.CharField(blank=True, default='', max_length=100)),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.Tag'),
        ),
        migrations.AddField(
            model_name='customvalue',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='api.Item'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
