# Generated by Django 4.0.6 on 2022-07-23 07:49

import celebrities.models
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
            name='Celebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='full name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=celebrities.models.get_photo_upload_path, verbose_name='Photo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('celebrity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrities.celebrity', verbose_name='Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(verbose_name='comment')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrities.photo', verbose_name='Photo')),
            ],
        ),
    ]
