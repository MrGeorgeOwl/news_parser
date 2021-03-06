# Generated by Django 3.0.5 on 2020-05-05 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0004_auto_20200505_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
