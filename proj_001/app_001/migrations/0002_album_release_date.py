# Generated by Django 3.1.3 on 2020-11-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_001', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
