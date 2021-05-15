# Generated by Django 3.2 on 2021-05-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210509_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=500, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url_to_image',
            field=models.URLField(max_length=500, null=True, verbose_name='image url'),
        ),
    ]