# Generated by Django 4.1.7 on 2023-03-15 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_appareils'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appareils',
            options={'ordering': ['name']},
        ),
    ]
