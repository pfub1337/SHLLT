from django.db import models
from django.db.models import F
# Create your models here.

class AnnotationManager(models.Manager):
    def __init__(self, **kwargs):
        super().__init__()
        self.annotations = kwargs

    def get_queryset(self):
        return super().get_queryset().annotate(**self.annotations)


class Team(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    win = models.IntegerField(default=0, verbose_name="Победа")
    draw = models.IntegerField(default=0, verbose_name="Ничья")
    lose = models.IntegerField(default=0, verbose_name="Поражения")
    _game = None
    _pts = None

    objects = AnnotationManager(
        game=F('win') + F('draw') + F('lose'),
        pts=F('win') * 3 + F('draw')
    )