# Generated by Django 4.0.6 on 2022-07-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torta', '0002_rename_project_torta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='torta',
            options={'ordering': ['-created'], 'verbose_name': 'torta', 'verbose_name_plural': 'tortas'},
        ),
        migrations.AlterField(
            model_name='torta',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='torta',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='torta',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='torta',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='torta',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición'),
        ),
    ]