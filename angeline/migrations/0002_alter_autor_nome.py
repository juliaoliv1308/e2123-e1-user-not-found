# Generated by Django 4.2.6 on 2023-11-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Author name'),
        ),
    ]
