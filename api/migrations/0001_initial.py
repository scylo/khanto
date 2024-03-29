# Generated by Django 4.1.5 on 2023-01-09 20:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('plataforma', models.CharField(max_length=50)),
                ('taxa_plataforma', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('codigo_imovel', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('limite_hospedes', models.PositiveIntegerField()),
                ('quantidade_banheiros', models.PositiveIntegerField()),
                ('aceita_animais', models.BooleanField(default=False)),
                ('valor_limpeza', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_ativacao', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('codigo_reserva', models.CharField(default=uuid.uuid4, editable=False, max_length=50)),
                ('data_checkin', models.DateField()),
                ('data_checkout', models.DateField()),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comentario', models.TextField(blank=True)),
                ('numero_hospedes', models.PositiveIntegerField()),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.anuncio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='anuncio',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.imovel'),
        ),
    ]
