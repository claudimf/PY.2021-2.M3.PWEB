from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Episodio, Revisor, Serie, Temporada, ReviewEpisodio
from .forms import SerieForm, TemporadaForm, RevisorForm, ReviewEpisodioForm, EpisodioForm

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

@login_required
@permission_required('seriados.view_serie', raise_exception=True)
def series_list(request):
  search = request.GET.get('search', "")
  objects = Serie.objects.filter(nome__contains=search)
  labels, rows = prepare_data_list(objects, ['nome'])
  context = {
    'title': "Séries",
    'labels': labels,
    'rows': rows,
    'detail_url': 'seriados:series_details',
    'list_url': 'seriados:series_list',
    'insert_url': 'seriados:serie_insert',
    'update_url': 'seriados:serie_update',
    'delete_url': 'seriados:serie_delete',
  }
  return render(request, 'generic/list.html', context)

@login_required
@permission_required('seriados.view_serie', raise_exception=True)
def series_details(request, pk):
  _object = get_object_or_404(Serie, pk=pk)
  context = {
    'title': "Série",
    'data': prepare_data_detail(_object, ['nome']),
    'update_url': 'seriados:serie_update',
    'delete_url': 'seriados:serie_delete',
    'list_url': 'seriados:series_list',
    'pk': pk,
  }
  return render(request, 'generic/details.html', context)

@login_required
@permission_required('seriados.add_serie', raise_exception=True)
def serie_insert(request):
  if request.method == 'GET':
    form = SerieForm()
  elif request.method == 'POST':
    form = SerieForm(request.POST)
    if form.is_valid():
      nome = form.cleaned_data['nome']
      obj = Serie(nome = nome)
      obj.save()
      return HttpResponseRedirect(
        reverse(
          'seriados:series_details',
          kwargs = {'pk': obj.pk}
          )
        )
  
  context = {
      'form': form,
      'target_url': 'seriados:serie_insert',
      'list_url': 'seriados:series_list',
      'title': 'Série',
  }

  return render(request, 'form/form_base.html', context)


class SerieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'seriados.change_serie'
  template_name = 'form/form_generic.html'
  model = Serie
  fields = ['nome']
  extra_context={
    'list_url': 'seriados:series_list',
    'title': 'Série',
    'action': 'Editar',
  }


class SerieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
  permission_required = 'seriados.delete_serie'
  template_name = "serie/serie_confirm_delete.html"
  model = Serie
  extra_context={
    'list_url': 'seriados:series_list',
    'detail_url': 'seriados:series_details',
    'title': 'Série',
    'action': 'Deletar',
  }

  def get_success_url(self):
    return reverse('seriados:serie_list')

@login_required
@permission_required('seriados.view_episodio', raise_exception=True)
def episodio_list(request):
  search = request.GET.get('search', "")
  objects = Episodio.objects.filter(titulo__contains=search)
  labels, rows = prepare_data_list(objects, ['titulo', 'data'])
  context = {
    'title': "Episódios",
    'labels': labels,
    'rows':rows,
    'detail_url': 'seriados:episodio_details',
    'list_url': 'seriados:episodio_list',
    'insert_url': 'seriados:episodio_insert',
    'update_url': 'seriados:episodio_update',
    'delete_url': 'seriados:episodio_delete',
  }
  return render(request, 'generic/list.html', context)

@login_required
@permission_required('seriados.view_episodio', raise_exception=True)
def episodio_details(request, pk):
  _object = get_object_or_404(Episodio, pk=pk)
  context = {
    'title': "Episódio",
    'data': prepare_data_detail(_object, ['titulo', 'data', 'temporada']),
    'update_url': 'seriados:episodio_update',
    'delete_url': 'seriados:episodio_delete',
    'list_url': 'seriados:episodio_list',
    'pk': pk,
  }
  return render(request, 'generic/details.html', context)

@login_required
@permission_required('seriados.view_episodio', raise_exception=True)
def episodio_nota_list(request, nota):
  search = request.GET.get('search', "")
  objects = Episodio.objects.filter(reviewepisodio__nota=nota if nota else search)
  context = {
    'objects': objects,
    'nota':nota,
    'detail_url': 'seriados:episodio_details',
  }
  return render(request, 'episodio/episodio_nota_list.html', context)


class EpisodioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
  permission_required = 'seriados.add_episodio'
  template_name = 'form/form_generic.html'
  form_class = EpisodioForm

  def get(self, request):
    form = EpisodioForm()
    
    context = {
      'form': form,
      'list_url': 'seriados:episodio_list',
      'title': 'Episódio',
      'action': 'Inserir',
    }

    return render(request, 'form/form_generic.html', context)


class EpisodioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'seriados.change_episodio'
  template_name = 'form/form_generic.html'
  model = Episodio
  fields = ['temporada', 'data', 'titulo']
  extra_context={
    'list_url': 'seriados:episodio_list',
    'title': 'Episódio',
    'action': 'Editar',
  }


class EpisodioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
  permission_required = 'seriados.delete_episodio'
  template_name = "episodio/episodio_confirm_delete.html"
  model = Episodio
  extra_context={
    'list_url': 'seriados:episodio_list',
    'detail_url': 'seriados:episodio_details',
    'title': 'Episódio',
    'action': 'Deletar',
  }

  def get_success_url(self):
    return reverse('seriados:episodio_list')


class EpisodioBuscaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  permission_required = 'seriados.view_episodio'
  template_name = 'episodio/episodio_busca_list.html'
  model = Episodio
  extra_context={
      'detail_url': 'seriados:episodio_details',
      'insert_url': 'seriados:episodio_insert',
      'title': 'Episódios',
  }

  def get_queryset(self):
      search = self.request.GET.get('search', "")
      q = Q(titulo__contains=search) | Q(temporada__serie__nome__contains=search)
      
      for term in search.split():
          q = q | Q(titulo__contains=term)
          q = q | Q(temporada__serie__nome__contains=term)
          try:
              i_term = int(term)
          except ValueError:
              pass
          else:
              q = q | Q(temporada__numero=i_term)

      qs = super().get_queryset().filter(q)
      
      return qs


class Contact(TemplateView):
  template_name = 'contact.html'


class HomeView(View):
  def get(self, request):
    return render(request, 'home.html', {})


class TemporadaListView(LoginRequiredMixin, PermissionRequiredMixin, View):
  permission_required = 'seriados.view_temporada'
  def get(self, request):
    search = request.GET.get('search', "")
    objects = Temporada.objects.filter(serie__nome__contains=search)
    labels, rows = prepare_data_list(objects, ['numero', 'serie'])
    context = {
      'book_list': objects,
      'title': 'Temporadas',
      'labels': labels,
      'rows': rows,
      'detail_url': 'seriados:temporada_details',
      'list_url': 'seriados:temporada_list',
      'insert_url': 'seriados:temporada_insert',
      'update_url': 'seriados:temporada_update',
      'delete_url': 'seriados:temporada_delete',
    }
    return render(request, 'generic/list.html', context)


class TemporadaDetailView(LoginRequiredMixin, PermissionRequiredMixin, View):
  permission_required = 'seriados.view_temporada'
  def get(self, request, pk):
    _object = get_object_or_404(Temporada, pk=pk)
    context = {
      'title': "Temporada",
      'object': _object,
      'update_url': 'seriados:temporada_update',
      'delete_url': 'seriados:temporada_delete',
      'list_url': 'seriados:temporada_list',
      'pk': pk,
    }
    return render(request, 'temporada/temporada_details.html', context)


class TemporadaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
  permission_required = 'seriados.add_temporada'
  template_name = "form/form_generic.html"
  form_class = TemporadaForm

  def get(self, request):
    form = TemporadaForm()
    
    context = {
      'form': form,
      'list_url': 'seriados:temporada_list',
      'title': 'Temporada',
      'action': 'Inserir',
    }

    return render(request, 'form/form_generic.html', context)


class TemporadaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'seriados.view_temporada', 'seriados.change_temporada'
  template_name = 'form/form_generic.html'
  model = Temporada
  fields = ['serie', 'numero']
  extra_context={
    'list_url': 'seriados:temporada_list',
    'title': 'Temporada',
    'action': 'Editar',
  }


class TemporadaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
  permission_required = 'seriados.delete_temporada'
  template_name = "temporada/temporada_confirm_delete.html"
  model = Temporada
  extra_context={
    'list_url': 'seriados:temporada_list',
    'detail_url': 'seriados:temporada_details',
    'title': 'Temporada',
    'action': 'Deletar',
  }

  def get_success_url(self):
    return reverse('seriados:temporada_list')


class RevisorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  permission_required = 'seriados.view_revisor'
  template_name = 'revisor/revisor_list.html'
  model = Revisor


class RevisorDetailView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  permission_required = 'seriados.view_revisor'
  template_name = 'revisor/revisor_details.html'
  model = ReviewEpisodio

  def get(self, request, pk):
    objects = ReviewEpisodio.objects.filter(revisor_id=pk)
    context = {
      'title': "Revisor",
      'list_url': 'seriados:revisor_list',
      'objects': objects,
      'pk': pk,
    }
    return render(request, 'revisor/revisor_details.html', context)


class RevisorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
  permission_required = 'seriados.add_revisor'
  template_name = "form/form_generic.html"
  form_class = RevisorForm

  def get(self, request):
    form = RevisorForm()

    context = {
      'form': form,
      'list_url': 'seriados:revisor_list',
      'title': 'Revisor',
    }

    return render(request, 'form/form_generic.html', context)


class RevisorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'seriados.change_revisor'
  template_name = 'form/form_generic.html'
  model = Revisor
  fields = ['user']
  extra_context={
    'list_url': 'seriados:revisor_list',
    'title': 'Revisor',
  }


class RevisorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
  permission_required = 'seriados.delete_revisor'
  template_name = "revisor/revisor_confirm_delete.html"
  model = Revisor
  extra_context={
    'list_url': 'seriados:revisor_list',
    'detail_url': 'seriados:revisor_details',
    'title': 'Revisor',
    'action': 'Deletar',
  }

  def get_success_url(self):
      return reverse('seriados:revisor_list')


class ReviewEpisodioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  permission_required = 'seriados.view_reviewepisodio'
  template_name = 'reviewepisodio/reviewepisodio_list.html'
  model = ReviewEpisodio


class ReviewEpisodioDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
  permission_required = 'seriados.view_reviewepisodio'
  template_name = 'reviewepisodio/reviewepisodio_details.html'
  model = ReviewEpisodio


class ReviewEpisodioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
  permission_required = 'seriados.add_reviewepisodio'
  template_name = "form/form_generic.html"
  form_class = ReviewEpisodioForm

  def get(self, request):
    form = ReviewEpisodioForm()

    context = {
      'form': form,
      'list_url': 'seriados:reviewepisodio_list',
      'title': 'Review de Episódio',
    }

    return render(request, 'form/form_generic.html', context)


class ReviewEpisodioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'seriados.change_reviewepisodio'
  template_name = 'form/form_generic.html'
  model = ReviewEpisodio
  fields = ['episodio', 'revisor', 'nota']
  extra_context={
    'list_url': 'seriados:reviewepisodio_list',
    'title': 'Review de Episódio',
  }


class ReviewEpisodioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
  permission_required = 'seriados.delete_reviewepisodio'
  template_name = "reviewepisodio/reviewepisodio_confirm_delete.html"
  model = ReviewEpisodio
  extra_context={
    'list_url': 'seriados:reviewepisodio_list',
    'detail_url': 'seriados:reviewepisodio_details',
    'title': 'Review de Episódio',
    'action': 'Deletar',
  }

  def get_success_url(self):
    return reverse('seriados:reviewepisodio_list')