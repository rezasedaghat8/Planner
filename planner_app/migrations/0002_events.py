# Generated by Django 5.0.1 on 2024-04-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
    ]
