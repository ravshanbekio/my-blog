# Generated by Django 4.1.6 on 2023-05-24 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_coursematerials_random_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerials',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='academy.course'),
        ),
    ]