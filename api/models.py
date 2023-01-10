from django.core.exceptions import ValidationError
from django.db import models

import uuid


class ClasseBase(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Imovel(ClasseBase):
    codigo_imovel = models.CharField(
        max_length=50,
        default=uuid.uuid4,
        editable=False
    )
    limite_hospedes = models.PositiveIntegerField()
    quantidade_banheiros = models.PositiveIntegerField()
    aceita_animais = models.BooleanField(default=False)
    valor_limpeza = models.DecimalField(max_digits=8, decimal_places=2)
    data_ativacao = models.DateField()


class Anuncio(ClasseBase):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='anuncios')
    plataforma = models.CharField(max_length=50)
    taxa_plataforma = models.DecimalField(max_digits=8, decimal_places=2)


class Reserva(ClasseBase):
    codigo_reserva = models.CharField(
        max_length=50,
        default=uuid.uuid4,
        editable=False
    )
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='reservas')
    data_checkin = models.DateField()
    data_checkout = models.DateField()
    preco_total = models.DecimalField(max_digits=8, decimal_places=2)
    comentario = models.TextField(blank=True)
    numero_hospedes = models.PositiveIntegerField()

    def clean(self):
        if self.data_checkout < self.data_checkin:
            raise ValidationError(
                'A data de check-out não pode ser maior que a de check-in'
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Reserva, self).save(*args, **kwargs)
