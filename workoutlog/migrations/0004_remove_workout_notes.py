# Generated by Django 4.1.5 on 2023-05-17 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workoutlog', '0003_alter_workout_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='notes',
        ),
    ]
