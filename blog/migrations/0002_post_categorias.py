# Generated by Django 4.2.16 on 2024-10-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(to='categorias.categoria'),
        ),
    ]
