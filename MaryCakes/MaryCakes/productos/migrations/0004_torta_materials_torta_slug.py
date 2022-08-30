# Generated by Django 4.0.6 on 2022-08-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_postres_idpostres_alter_torta_idtorta'),
    ]

    operations = [
        migrations.AddField(
            model_name='torta',
            name='materials',
            field=models.TextField(default='null', verbose_name='Materiales'),
        ),
        migrations.AddField(
            model_name='torta',
            name='slug',
            field=models.SlugField(default='null', max_length=200),
        ),
    ]