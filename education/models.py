from django.db import models

# Create your models here.

class BotDialog(models.Model):
    #ans = models.TextField(verbose_name="Бот спрашивает")
    dialog = models.TextField(verbose_name="Кусок диалога")
    owner = models.BooleanField(verbose_name="Принадлежность боту(если checkbox стоит, то боту принадлежит)")

class Connections(models.Model):
    firstfrase = models.IntegerField(verbose_name="id первой фразы")
    secondfrase = models.IntegerField(verbose_name="id вторая фраза")
    balls = models.IntegerField(verbose_name="Количество баллов")

class Courses(models.Model):
    page_title = models.CharField(max_length = 5, verbose_name="Ссылка на страницу")
    title = models.CharField(max_length = 100, verbose_name="Название курса")
    school = models.IntegerField(verbose_name="id учреждения")
    duration = models.IntegerField(verbose_name="Длительность курса")
    type = models.CharField(max_length = 50, verbose_name="Тип курса")
    price = models.IntegerField(verbose_name="Стоимость курса")
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    rate_students = models.FloatField(verbose_name="Оценка студентами")
    rate_auditors = models.FloatField(verbose_name="Оценка аудиторами")

class Schools(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название учреждения")
