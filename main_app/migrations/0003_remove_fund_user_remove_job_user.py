# Generated by Django 4.1.3 on 2022-12-14 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_fund_deadline_alter_job_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
    ]
