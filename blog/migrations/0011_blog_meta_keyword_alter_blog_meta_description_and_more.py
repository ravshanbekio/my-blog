# Generated by Django 4.1.6 on 2023-03-21 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_preview_image_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='meta_keyword',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_description',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_description_en',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_description_ru',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_description_uz',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
