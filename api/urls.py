from django.urls import path
from .views import (
    ImovelList, ImovelView,
    AnuncioList, AnuncioView,
    ReservaList, ReservaView,
)

urlpatterns = [
    path('imovel/', ImovelList.as_view(), name='imovel-list'),
    path('imovel/<int:pk>', ImovelView.as_view(), name='imovel-view'),

    path('anuncio/', AnuncioList.as_view(), name='anuncio-list'),
    path('anuncio/<int:pk>', AnuncioView.as_view(), name='anuncio-view'),

    path('reserva/', ReservaList.as_view(), name='reserva-list'),
    path('reserva/<int:pk>', ReservaView.as_view(), name='reserva-view'),
]