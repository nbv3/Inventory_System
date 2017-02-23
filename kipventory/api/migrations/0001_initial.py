# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 06:32
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
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(choices=[('Item Modification', 'Item Modification'), ('Item Creation', 'Item Creation'), ('Item Deletion', 'Item Deletion')], max_length=20)),
                ('affected_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affected_user', to=settings.AUTH_USER_MODEL)),
                ('initiating_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiating_user', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.CreateModel(
            name='NewUserRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('comment', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_open', models.DateTimeField(blank=True, null=True)),
                ('open_comment', models.TextField(blank=True, default='', max_length=500)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('closed_comment', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('O', 'Outstanding'), ('A', 'Approved'), ('D', 'Denied')], default='O', max_length=10)),
                ('administrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests_administrated', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Item')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_items', to='api.Request')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Acquisition', 'Acquisition'), ('Loss', 'Loss')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField()),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
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
