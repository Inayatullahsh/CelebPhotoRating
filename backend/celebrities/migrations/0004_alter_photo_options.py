# Generated by Django 4.0.6 on 2022-07-25 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0003_alter_celebrity_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-created'], 'verbose_name': 'Celeb Photo', 'verbose_name_plural': 'Celeb Photos'},
        ),
    ]