from rest_framework import serializers
from .models import Imovel, Anuncio, Reserva


class ImovelSerializer(serializers.ModelSerializer):
   class Meta:
      model = Imovel
      fields = ('__all__')


class AnuncioSerializer(serializers.ModelSerializer):

   class Meta:
      model = Anuncio
      fields = ('__all__')


class ReservaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Reserva
      fields = ('__all__')
