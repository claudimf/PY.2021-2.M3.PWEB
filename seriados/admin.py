from django.contrib import admin
from . import models

admin.site.register(models.Serie)
admin.site.register(models.Temporada)
admin.site.register(models.Episodio)
admin.site.register(models.Revisor)
admin.site.register(models.ReviewEpisodio)
