# Generated by Django 3.0.5 on 2020-05-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0002_auto_20200505_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssite',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newssite',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
