# Generated by Django 4.0.6 on 2022-07-23 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celebrity',
            options={'ordering': ['full_name'], 'verbose_name': 'Celebrity', 'verbose_name_plural': 'Celebrities'},
        ),
    ]