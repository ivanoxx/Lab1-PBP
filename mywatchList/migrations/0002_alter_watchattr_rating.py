# Generated by Django 4.1 on 2022-09-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchattr',
            name='rating',
            field=models.FloatField(),
        ),
    ]
