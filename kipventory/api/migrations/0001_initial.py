# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 15:12
from __future__ import unicode_literals

import api.models
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
            name='ApprovedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('request_type', models.CharField(choices=[('loan', 'Loan'), ('disbursement', 'Disbursement')], default='loan', max_length=15)),
            ],
            options={
                'ordering': ('item__name',),
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default=api.models.uuid_to_str, max_length=256, unique=True)),
            ],
            options={
                'ordering': ('tag',),
            },
        ),
        migrations.CreateModel(
            name='BulkImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('loan', 'Loan'), ('disbursement', 'Disbursement')], default='disbursement', max_length=15)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Asset')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_assets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('item__name',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('request_type', models.CharField(choices=[('loan', 'Loan'), ('disbursement', 'Disbursement')], default='disbursement', max_length=15)),
            ],
            options={
                'ordering': ('item__name',),
            },
        ),
        migrations.CreateModel(
            name='CustomAssetValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Single', models.CharField(blank=True, default='', max_length=256)),
                ('Multi', models.TextField(blank=True, default='', max_length=1024)),
                ('Int', models.IntegerField(blank=True, default=0)),
                ('Float', models.FloatField(blank=True, default=0.0)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='api.Asset')),
            ],
            options={
                'ordering': ('field__name',),
            },
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('private', models.BooleanField(default=False)),
                ('field_type', models.CharField(choices=[('Single', 'Single-line text'), ('Multi', 'Multi-line text'), ('Int', 'Integer'), ('Float', 'Float')], default='Single', max_length=10)),
                ('asset_tracked', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CustomValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Single', models.CharField(blank=True, default='', max_length=256)),
                ('Multi', models.TextField(blank=True, default='', max_length=1024)),
                ('Int', models.IntegerField(blank=True, default=0)),
                ('Float', models.FloatField(blank=True, default=0.0)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_values', to='api.CustomField', to_field='name')),
            ],
            options={
                'ordering': ('field__name',),
            },
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('minimum_stock', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('model_no', models.CharField(blank=True, default='', max_length=256)),
                ('description', models.TextField(blank=True, default='', max_length=1024)),
                ('has_assets', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_loaned', models.DateTimeField(auto_now_add=True)),
                ('date_returned', models.DateTimeField(blank=True, null=True)),
                ('quantity_loaned', models.PositiveIntegerField(default=0)),
                ('quantity_returned', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='LoanReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('body', models.TextField(max_length=1024)),
                ('subject', models.CharField(default='', max_length=128)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(blank=True, max_length=1024, null=True)),
                ('default_item', models.CharField(blank=True, max_length=256, null=True)),
                ('default_initiating_user', models.CharField(blank=True, max_length=256, null=True)),
                ('default_affected_user', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(choices=[('Item Modification', 'Item Modification'), ('Item Creation', 'Item Creation'), ('Item Deletion', 'Item Deletion'), ('Request Item Creation', 'Request Item Creation'), ('Request Item Approval: Loan', 'Request Item Approval: Loan'), ('Request Item Approval: Disburse', 'Request Item Approval: Disburse'), ('Request Item Loan Changed to Disburse', 'Request Item Loan Changed to Disburse'), ('Request Item Loan Modify', 'Request Item Loan Modify'), ('Request Item Denial', 'Request Item Denial'), ('User Creation', 'User Creation'), ('Transaction Creation', 'Transaction Creation')], max_length=50)),
                ('affected_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='affected_user', to=settings.AUTH_USER_MODEL)),
                ('initiating_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='initiating_user', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Item')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_open', models.DateTimeField(auto_now_add=True)),
                ('open_comment', models.TextField(blank=True, default='', max_length=1024)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('closed_comment', models.TextField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('O', 'Outstanding'), ('A', 'Approved'), ('D', 'Denied')], default='O', max_length=15)),
                ('administrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests_administrated', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_open',),
            },
        ),
        migrations.CreateModel(
            name='RequestedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('request_type', models.CharField(choices=[('loan', 'Loan'), ('disbursement', 'Disbursement')], default='loan', max_length=15)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_items', to='api.Item')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_items', to='api.Request')),
            ],
            options={
                'ordering': ('item__name',),
            },
        ),
        migrations.CreateModel(
            name='SubjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Acquisition', 'Acquisition'), ('Loss', 'Loss')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('comment', models.CharField(blank=True, max_length=1024, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Request'),
        ),
        migrations.AddField(
            model_name='loan',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='api.Request'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.Tag'),
        ),
        migrations.AddField(
            model_name='disbursement',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
        ),
        migrations.AddField(
            model_name='disbursement',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disbursements', to='api.Request'),
        ),
        migrations.AddField(
            model_name='customvalue',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='api.Item'),
        ),
        migrations.AddField(
            model_name='customassetvalue',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_values', to='api.CustomField', to_field='name'),
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
        migrations.AddField(
            model_name='asset',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='api.Item'),
        ),
        migrations.AddField(
            model_name='approveditem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
        ),
        migrations.AddField(
            model_name='approveditem',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_items', to='api.Request'),
        ),
    ]
