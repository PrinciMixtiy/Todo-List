# Generated by Django 4.2.7 on 2024-01-06 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2024, 1, 6, 8, 33, 37, 590229, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
