from django.urls import path, re_path, include, register_converter
from django.views.generic import TemplateView

from . import views

app_name = 'seriados'

urlpatterns = [
    path('series/', views.series_list, name='series_list'),
    path('series/<int:pk>/', views.series_details, name='series_details'),
    path('episodios/', views.episodio_list, name='episodio_list'),
    path('episodios/<int:pk>/', views.episodio_details, name='episodio_details'),
    path('episodios/nota/<str:nota>/', views.episodio_nota_list, name='episodio_nota_list'),
    path('sobre/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contato/', views.Contact.as_view(), name='contact'),
    path('', views.HomeView.as_view(), name='home'),
    path('temporadas/', views.TemporadaListView.as_view(), name='temporadas'),
    path('serie/inserir/', views.serie_insert, name='serie_insert'),
    path('temporada/', views.TemporadaListView.as_view(),name='temporada_list'),
    path('temporada/<int:pk>/', views.TemporadaDetail.as_view(),name='temporada_details'),
    path('temporada/inserir/', views.TemporadaCreateView.as_view(),name='temporada_insert'),
    path('episodio/inserir/', views.EpisodioCreateView.as_view(), name='episodio_insert'),
    path('temporada/<int:pk>/editar/', views.TemporadaUpdateView.as_view(), name='temporada_update'),
    path('temporada/<int:pk>/excluir/', views.TemporadaDeleteView.as_view(), name='temporada_excluir'),
]