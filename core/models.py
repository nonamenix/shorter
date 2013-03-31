# -*- coding: utf-8 -*-
from django.db import models
import datetime
import random

# Create your models here.


def generateURN():
    LOW_CHARS = range(97, 123)
    HIGH_CHARS = range(65, 91)
    DIGITS = range(48, 58)
    chars = [chr(char) for char in list( set(LOW_CHARS) | set(HIGH_CHARS) | set(DIGITS))]

    return "".join([chars[int(random.random() * len(chars))] for i in range(8)])

class Short(models.Model):
    full_uri = models.URLField(help_text=u"Укажите ссылку, на которую хотите сделать short")
    short_urn = models.SlugField(default=generateURN, help_text=u"Короткая ссылка")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text=u"Время создания")
    conversions = models.IntegerField(default=0, help_text=u"Количество переходов")

    class Meta:
        ordering = ('-created_at',)

    def increase_conversions(self):
        self.conversions += 1
        self.save()