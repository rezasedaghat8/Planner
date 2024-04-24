# Generated by Django 5.0.1 on 2024-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0003_rename_id_number_events_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id_number', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
