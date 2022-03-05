from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from .models import Serie, Temporada, Episodio
from django.views import View
from django.views.generic import TemplateView, ListView


class Contact(TemplateView):
  template_name = 'contact.html'


class HomeView(View):
  def get(self, request):
    return render(request, 'home.html', {})


class TemporadaListView(ListView):
  template_name = 'temporada_list.html'
  model = Temporada


def prepare_data_list(objects, fields_name):
  labels = list()
  for field_name in fields_name:
    field = objects.model._meta.get_field(field_name)
    labels.append(field.verbose_name)
    
  rows = list()
  for _object in objects:
    row = dict()
    rows.append(row)
    row['pk'] = _object.pk
    row['data'] = list()
    for field_name in fields_name:
      row['data'].append(getattr(_object, field_name))
  
  return labels, rows

def prepare_data_detail(_object, fields_name):
  data = model_to_dict(_object)
  rows = list()
  for field_name in fields_name:
    field = _object._meta.get_field(field_name)
    rows.append({'label': field.verbose_name, 'value': data[field_name]})
    return rows

def series_list(request):
  objects = Serie.objects.all()
  labels, rows = prepare_data_list(objects, ['nome'])
  context = {
    'title': "Series",
    'labels': labels,
    'rows': rows,
    'detail_url': 'seriados:series_details',
    }

  return render(request, 'list.html', context)

def series_details(request, pk):
  _object = get_object_or_404(Serie, pk=pk)
  context = {
    'title': "Serie",
    'data': prepare_data_detail(_object, ['nome']),
    }
  return render(request, 'details.html', context)

def episodio_list(request):
  search = request.GET.get('search', "")
  objects = Episodio.objects.filter(titulo__startswith=search)
  labels, rows = prepare_data_list(objects, ['titulo', 'data'])
  context = {
    'title': "Episódios",
    'labels': labels,
    'rows':rows,
    'detail_url': 'seriados:episodio_details',
    }

  return render(request, 'list.html', context)

def episodio_details(request, pk):
  _object = get_object_or_404(Episodio, pk=pk)
  context = {
    'title': "Episódio",
    'data': prepare_data_detail(_object, ['titulo', 'data', 'temporada']),
    }
  
  return render(request, 'details.html', context)

def episodio_nota_list(request, nota):
  return render(request, 'home.html', {})