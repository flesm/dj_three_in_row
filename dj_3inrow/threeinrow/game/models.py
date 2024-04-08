from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Номер команды')
    name = models.CharField(max_length=50, unique=True, verbose_name='Название команды')
    total_score = models.IntegerField(default=0, verbose_name='Счёт команды')