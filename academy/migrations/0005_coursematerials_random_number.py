# Generated by Django 4.1.6 on 2023-04-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_course_students_alter_course_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerials',
            name='random_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
