# Generated by Django 4.0.5 on 2022-06-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imobiliaria', '0002_alter_fotos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='foto',
            field=models.ImageField(blank=True, help_text='Escolha uma foto.', upload_to='media/fotos/%Y/%m/%d', verbose_name='Foto'),
        ),
    ]
