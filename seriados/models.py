from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Serie(models.Model):
  nome = models.CharField(max_length=70, verbose_name="Nome")

  class Meta:
    verbose_name = "Série"
    verbose_name_plural = "Séries"

  def __str__(self):
    return self.nome
  
  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('seriados:series_details', kwargs={'pk' : self.pk})


class Temporada(models.Model):
  numero = models.IntegerField(verbose_name="Número")
  serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name="Série")

  class Meta:
    verbose_name = "Temporada"
    verbose_name_plural = "Temporadas"

  def __str__(self):
    return f"{self.serie.nome}: {self.numero}"
  
  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('seriados:temporada_details', kwargs={'pk' : self.pk})


class Episodio(models.Model):
  data = models.DateField(verbose_name="Data")
  titulo = models.CharField(max_length=200, verbose_name="Título")
  temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, verbose_name="Temporada")

  class Meta:
    verbose_name = "Episódio"
    verbose_name_plural = "Episódios"

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
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuário")
  reviews_episodios = models.ManyToManyField(Episodio, through='ReviewEpisodio', related_name='review', verbose_name="Review do Episódio")

  class Meta:
    verbose_name = "Revisor"
    verbose_name_plural = "Revisores"
  
  def __str__(self):
    return f"{self.user}"
  
  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('seriados:revisor_details', kwargs={'pk' : self.pk})


class ReviewEpisodio(models.Model):
  NOTA_A = 'A'
  NOTA_B = 'B'
  NOTA_C = 'C'

  NOTAS_CHOICES = [
      (NOTA_A, "Excelente"),
      (NOTA_B, "Bom"),
      (NOTA_C, "Ruim"),
  ]

  episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE, verbose_name="Episódio")
  revisor = models.ForeignKey(Revisor, on_delete=models.CASCADE, verbose_name="Revisor")
  nota = models.CharField(
    max_length=1,
    choices=NOTAS_CHOICES,
    default=NOTA_B,
    verbose_name="Nota"
  )

  class Meta:
    verbose_name = "Review do Episódio"
    verbose_name_plural = "Reviews dos Episódios"

  def __str__(self):
    return f"{self.episodio}: {self.revisor}"
  
  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('seriados:reviewepisodio_details', kwargs={'pk' : self.pk})