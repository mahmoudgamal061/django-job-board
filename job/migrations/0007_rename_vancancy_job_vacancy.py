# Generated by Django 4.1.5 on 2023-01-23 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='vancancy',
            new_name='vacancy',
        ),
    ]
