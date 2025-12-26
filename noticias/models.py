from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    resumen = models.TextField(max_length=300)
    contenido = models.TextField()

    imagen = models.ImageField(
        upload_to='noticias/',
        blank=True,
        null=True
    )

    autor = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)
    publicada = models.BooleanField(default=True)
    creada = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
