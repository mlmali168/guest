# Generated by Django 2.0 on 2018-08-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20180803_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='limit',
            field=models.IntegerField(null=True),
        ),
    ]