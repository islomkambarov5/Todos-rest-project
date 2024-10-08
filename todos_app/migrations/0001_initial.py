# Generated by Django 5.0.7 on 2024-07-27 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название задания')),
                ('description', models.TextField(verbose_name='О задании')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Выполнено?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда добавлено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда в последний раз изменнено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Какой пользователь')),
            ],
        ),
    ]
