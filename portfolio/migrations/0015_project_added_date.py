# Generated by Django 4.1.6 on 2023-07-21 04:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_project_about_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='added_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]