# Generated by Django 4.1.5 on 2023-01-09 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios', to='api.imovel'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='anuncio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='api.anuncio'),
        ),
    ]