# Generated by Django 5.0.1 on 2024-04-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0006_event_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_project',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
