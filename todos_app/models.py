from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Todos(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название задания')
    description = models.TextField(verbose_name='О задании')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Когда добавлено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Когда в последний раз изменнено')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Какой пользователь')

    def __str__(self):
        return self.title
