# Generated by Django 3.0.3 on 2020-05-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_marksheet_passed'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='tTime',
            field=models.IntegerField(default=0),
        ),
    ]