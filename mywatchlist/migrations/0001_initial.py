# Generated by Django 4.1 on 2022-09-26 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchAttr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('release_date', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
