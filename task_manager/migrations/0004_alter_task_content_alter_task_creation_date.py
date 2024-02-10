# Generated by Django 4.2.7 on 2024-01-06 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_task_owner_alter_task_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
