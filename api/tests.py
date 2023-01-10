from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from .models import Imovel, Anuncio, Reserva
from .views import (
	ImovelList,
	ImovelView,
	AnuncioList,
	AnuncioView,
	ReservaList,
	ReservaView
)

class TCBase(APITestCase):
	def setUp(self):
		self.factory = APIRequestFactory()

		self.imovel_1 = Imovel.objects.create(
			limite_hospedes=11,
			quantidade_banheiros=11,
			aceita_animais=True,
			valor_limpeza=11,
			data_ativacao='2022-05-01',
		)
		self.anuncio_1 = Anuncio.objects.create(
			plataforma='AirBnb',
		    taxa_plataforma=0.16,
		    imovel=self.imovel_1
		)
		self.reserva_1 = Reserva.objects.create(
			data_checkin='2022-05-01',
		    data_checkout='2022-05-05',
		    preco_total=500.00,
		    comentario='Excelente imóvel, recomendo!',
		    numero_hospedes=4,
		    anuncio=self.anuncio_1
		)


class ImovelTestCase(TCBase):
	'''
	Deve ser possível buscar uma lista de imóveis,
	buscar um imóvel individual, criar, alterar e deletar um imóvel
	'''

	def setUp(self):
		super(ImovelTestCase, self).setUp()

	def test_list(self):
		request = self.factory.get(reverse('imovel-list'))
		response = ImovelList.as_view()(request)
		self.assertEqual(response.status_code, 200)

	def test_view(self):
		request = self.factory.get(
			reverse('imovel-view', args=[self.imovel_1.pk])
		)
		response = ImovelView.as_view()(request, pk=self.imovel_1.pk)
		self.assertEqual(response.status_code, 200)

	def test_edit(self):
		request = self.factory.patch(
			reverse('imovel-view', args=[self.imovel_1.pk]),
			data={'aceita_animais': False}
		)
		response = ImovelView.as_view()(request, pk=self.imovel_1.pk)
		self.assertEqual(response.status_code, 200)

	def test_delete(self):
		request = self.factory.delete(
			reverse('imovel-view', args=[self.imovel_1.pk])
		)
		response = ImovelView.as_view()(request, pk=self.imovel_1.pk)
		self.assertEqual(response.status_code, 204)


class AnuncioTestCase(TCBase):
	'''
	Deve ser possível buscar uma lista de anúncios, 
	buscar um anúncio individual, criar um anúncio e alterar um anúncio, 
	mas não apagá-lo
	'''

	def setUp(self):
		super(AnuncioTestCase, self).setUp()

	def test_list(self):
		request = self.factory.get(reverse('anuncio-list'))
		response = AnuncioList.as_view()(request)
		self.assertEqual(response.status_code, 200)

	def test_view(self):
		request = self.factory.get(
			reverse('anuncio-view', args=[self.anuncio_1.pk])
		)
		response = AnuncioView.as_view()(request, pk=self.anuncio_1.pk)
		self.assertEqual(response.status_code, 200)

	def test_edit(self):
		request = self.factory.patch(
			reverse('anuncio-view', args=[self.anuncio_1.pk]),
			data={'taxa_plataforma': 0.20}
		)
		response = AnuncioView.as_view()(request, pk=self.anuncio_1.pk)
		self.assertEqual(response.status_code, 200)

	def test_delete(self):
		request = self.factory.delete(
			reverse('anuncio-view', args=[self.anuncio_1.pk])
		)
		response = AnuncioView.as_view()(request, pk=self.anuncio_1.pk)
		self.assertEqual(response.status_code, 405)


class ReservaTestCase(TCBase):
	'''
	Deve ser possível buscar uma lista de reservas, 
	buscar uma reserva individual, criar uma reserva e deletar uma reserva, 
	mas não alterá-la;
	'''

	def setUp(self):
		super(ReservaTestCase, self).setUp()

	def test_list(self):
		request = self.factory.get(reverse('reserva-list'))
		response = ReservaList.as_view()(request)
		self.assertEqual(response.status_code, 200)

	def test_view(self):
		request = self.factory.get(
			reverse('reserva-view', args=[self.reserva_1.pk])
		)
		response = ReservaView.as_view()(request, pk=self.reserva_1.pk)
		self.assertEqual(response.status_code, 200)

	def test_edit(self):
		request = self.factory.patch(
			reverse('reserva-view', args=[self.reserva_1.pk]),
			data={'numero_hospedes': 10}
		)
		response = ReservaView.as_view()(request, pk=self.reserva_1.pk)
		self.assertEqual(response.status_code, 405)

	def test_delete(self):
		request = self.factory.delete(
			reverse('reserva-view', args=[self.reserva_1.pk])
		)
		response = ReservaView.as_view()(request, pk=self.reserva_1.pk)
		self.assertEqual(response.status_code, 204)
