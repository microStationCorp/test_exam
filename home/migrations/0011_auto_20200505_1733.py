# Generated by Django 3.0.3 on 2020-05-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200505_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marksheet',
            name='mark',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='marksheet',
            name='percentage',
            field=models.FloatField(default=0),
        ),
    ]