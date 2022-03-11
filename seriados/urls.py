from django.urls import path, re_path, include, register_converter
from django.views.generic import TemplateView

from . import views

app_name = 'seriados'

urlpatterns = [
    path('series/', views.series_list, name='series_list'),
    path('series/<int:pk>', views.series_details, name='series_details'),
    path('series/inserir/', views.serie_insert, name='serie_insert'),
    path('series/<int:pk>/editar/', views.SerieUpdateView.as_view(), name='serie_update'),
    path('series/<int:pk>/excluir/', views.SerieDeleteView.as_view(), name='serie_delete'),

    path('episodios/', views.episodio_list, name='episodio_list'),
    path('episodios/<int:pk>/', views.episodio_details, name='episodio_details'),
    path('episodios/nota/<str:nota>/', views.episodio_nota_list, name='episodio_nota_list'),
    path('episodios/inserir/', views.EpisodioCreateView.as_view(), name='episodio_insert'),
    path('episodios/<int:pk>/editar/', views.EpisodioUpdateView.as_view(), name='episodio_update'),
    path('episodios/<int:pk>/excluir/', views.EpisodioDeleteView.as_view(), name='episodio_delete'),
    path('episodios/busca/', views.EpisodioBuscaListView.as_view(), name='episodio_busca_list'),

    path('temporadas/', views.TemporadaListView.as_view(), name='temporada_list'),
    path('temporadas/<int:pk>/', views.TemporadaDetailView.as_view(), name='temporada_details'),
    path('temporadas/inserir/', views.TemporadaCreateView.as_view(), name='temporada_insert'),
    path('temporadas/<int:pk>/editar/', views.TemporadaUpdateView.as_view(), name='temporada_update'),
    path('temporadas/<int:pk>/excluir/', views.TemporadaDeleteView.as_view(), name='temporada_delete'),

    path('revisores/', views.RevisorListView.as_view(), name='revisor_list'),
    path('revisores/<int:pk>', views.RevisorDetailView.as_view(), name='revisor_details'),
    path('revisores/inserir/', views.RevisorCreateView.as_view(), name='revisor_insert'),
    path('revisores/<int:pk>/editar/', views.RevisorUpdateView.as_view(), name='revisor_update'),
    path('revisores/<int:pk>/excluir/', views.RevisorDeleteView.as_view(), name='revisor_delete'),

    path('reviewepisodios/', views.ReviewEpisodioListView.as_view(), name='reviewepisodio_list'),
    path('reviewepisodios/<int:pk>', views.ReviewEpisodioDetailView.as_view(), name='reviewepisodio_details'),
    path('reviewepisodios/inserir/', views.ReviewEpisodioCreateView.as_view(), name='reviewepisodio_insert'),
    path('reviewepisodios/<int:pk>/editar/', views.ReviewEpisodioUpdateView.as_view(), name='reviewepisodio_update'),
    path('reviewepisodios/<int:pk>/excluir/', views.ReviewEpisodioDeleteView.as_view(), name='reviewepisodio_delete'),

    path('sobre/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contato/', views.Contact.as_view(), name='contact'),

    path('', views.HomeView.as_view(), name='home'),
]