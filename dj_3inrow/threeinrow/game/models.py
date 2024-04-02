from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Номер команды')
    name = models.CharField(max_length=50, unique=True, verbose_name='Название команды')
    total_score = models.IntegerField(default=0, verbose_name='Счёт команды')

    # def update_total_score(self):
    #     self.total_score = sum(user.score for user in self.user_set.all())
    #     self.save()


# class User(models.Model):
#     id_user = models.AutoField(primary_key=True, verbose_name='Номер пользователя')
#     session_key = models.CharField(max_length=40, unique=True, verbose_name='Ключ сессии пользователя')
#     score = models.IntegerField(default=0, verbose_name='Счёт пользователя')
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда пользователя')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.team.update_total_score()