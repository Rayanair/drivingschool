# Generated by Django 5.0.4 on 2024-05-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving_school', '0002_appointment_hours_student_address_student_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='total_hours',
            field=models.IntegerField(default=0),
        ),
    ]
