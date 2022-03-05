from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Serie(models.Model):
  nome = models.CharField(max_length=70)

  def __str__(self):
    return self.nome


class Temporada(models.Model):
  numero = models.IntegerField()
  serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.serie.nome}: {self.numero}"


class Episodio(models.Model):
  data = models.DateField()
  titulo = models.CharField(max_length=200)
  temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
  
  def __str__(self):
    nome_serie = self.temporada.serie.nome
    return f"{nome_serie} - {self.temporada.numero}: {self.titulo}"    

  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('seriados:episodio_details', kwargs={'pk' : self.pk})
  
  def eh_antigo(self):
    import datetime
    if self.data < datetime.date(2000, 1, 1):
      return True
    return False


class Revisor(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	reviews_episodios = models.ManyToManyField(Episodio, through='ReviewEpisodio')


class ReviewEpisodio(models.Model):
  NOTA_A = 'A'
  NOTA_B = 'B'
  NOTA_C = 'C'
  NOTAS_CHOICES = [ 
    (NOTA_A, _("Excelente")), 
    (NOTA_B, _("Bom")), 
    (NOTA_C, _("Ruim")), 
  ]
  episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
  revisor = models.ForeignKey(Revisor, on_delete=models.CASCADE)
  nota = models.CharField( 
    max_length=1, 
    choices=NOTAS_CHOICES, 
    default = NOTA_B 
  )