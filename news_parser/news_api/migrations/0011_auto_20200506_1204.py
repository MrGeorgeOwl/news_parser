# Generated by Django 3.0.5 on 2020-05-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0010_auto_20200505_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]