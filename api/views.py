from rest_framework import generics

from .models import Imovel, Anuncio, Reserva
from .serializers import ImovelSerializer, AnuncioSerializer, ReservaSerializer


class ImovelList(generics.ListCreateAPIView):
	serializer_class = ImovelSerializer
	queryset = Imovel.objects.all()


class ImovelView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ImovelSerializer
	queryset = Imovel.objects.all()


class AnuncioList(generics.ListCreateAPIView):
	serializer_class = AnuncioSerializer
	queryset = Anuncio.objects.all()


class AnuncioView(generics.RetrieveUpdateAPIView):
	serializer_class = AnuncioSerializer
	queryset = Anuncio.objects.all()


class ReservaList(generics.ListCreateAPIView):
	serializer_class = ReservaSerializer
	queryset = Reserva.objects.all()


class ReservaView(generics.RetrieveDestroyAPIView):
	serializer_class = ReservaSerializer
	queryset = Reserva.objects.all()
