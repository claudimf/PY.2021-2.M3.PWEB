from django import forms
from .models import Serie, Temporada, Episodio, Revisor, ReviewEpisodio


class SerieForm(forms.Form):
	nome = forms.CharField(label="Nome da Série", max_length=70)


class TemporadaForm(forms.ModelForm):
	class Meta:
		model = Temporada
		fields = ['numero', 'serie']


class RevisorForm(forms.ModelForm):
    class Meta:
        model = Revisor
        fields = ['user']


class ReviewEpisodioForm(forms.ModelForm):
    class Meta:
        model = ReviewEpisodio
        fields = ['episodio', 'revisor', 'nota']


class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = ['temporada', 'data', 'titulo']