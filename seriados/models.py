from django.db import models

class Serie(models.Model):
  nome = models.CharField(max_length=70)

  def __str__(self):
    return self.nome


class Temporada(models.Model):
	numero = models.IntegerField()
	serie = models.ForeignKey(Serie, on_delete=models.CASCADE)


class Episodio(models.Model):
	data = models.DateField()
	titulo = models.CharField(max_length=200)
	temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
	def __str__(self):
		return self.titulo
