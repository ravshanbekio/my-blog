# Generated by Django 4.1.6 on 2023-04-21 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_education_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Education',
            new_name='Experience',
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name_plural': 'Experience'},
        ),
    ]
