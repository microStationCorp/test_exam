# Generated by Django 3.0.3 on 2020-05-11 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200511_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='objection',
            name='dateOfReport',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
