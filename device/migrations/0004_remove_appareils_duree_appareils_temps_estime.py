# Generated by Django 4.1.7 on 2023-03-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_alter_appareils_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appareils',
            name='duree',
        ),
        migrations.AddField(
            model_name='appareils',
            name='temps_estime',
            field=models.IntegerField(null=True),
        ),
    ]
