from django.urls import path, re_path, include, register_converter
from . import views

app_name = 'seriados'

urlpatterns = [
    path('series/', views.series_lista, name='series_lista'),
]