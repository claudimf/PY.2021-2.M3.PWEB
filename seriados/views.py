from django.shortcuts import render
from .models import Serie

def series_lista(request):
	lista_series = Serie.objects.all()
	context = {'lista_series': lista_series}
	return render(request, 'series_lista.html', context)
