# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pic', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('born', models.DateField()),
                ('status', models.CharField(max_length=45)),
                ('sex', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('need_compation', models.CharField(max_length=255)),
                ('with_dogs', models.CharField(max_length=45)),
                ('with_kids', models.CharField(max_length=45)),
                ('home_env', models.CharField(max_length=45)),
                ('special_need', models.CharField(max_length=255)),
                ('comment_top', models.CharField(max_length=255)),
                ('comment_main', models.TextField()),
                ('comment_bot', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picturetocat', to='spca_app.Cat')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pic', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=45)),
                ('breed', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('size', models.CharField(max_length=45)),
                ('obedience', models.CharField(max_length=45)),
                ('energy_level', models.CharField(max_length=45)),
                ('with_dogs', models.CharField(max_length=45)),
                ('with_kids', models.CharField(max_length=45)),
                ('with_cats', models.CharField(max_length=45)),
                ('comment_main', models.TextField()),
                ('comment_bot', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dog_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picturetodog', to='spca_app.Dog')),
            ],
        ),
    ]
