# Generated by Django 4.2.6 on 2023-11-03 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=100)),
                ('data_aluguel', models.DateTimeField(auto_now_add=True)),
                ('data_devolucao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('resumo', models.TextField()),
                ('linkimg', models.ImageField(upload_to='livros/')),
                ('pdf', models.FileField(upload_to='livros/')),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3)),
                ('sub_categoria', models.CharField(blank=True, max_length=255)),
                ('estoque', models.PositiveIntegerField()),
                ('aluguel', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='angeline.aluguel')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angeline.categoria')),
            ],
        ),
    ]
