# Generated by Django 4.2.6 on 2023-11-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
