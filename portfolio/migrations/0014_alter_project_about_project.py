# Generated by Django 4.1.6 on 2023-07-21 04:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='about_project',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
