# Generated by Django 3.0.5 on 2020-05-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0007_auto_20200505_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
