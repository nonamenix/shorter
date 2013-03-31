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
    full_uri = models.URLField( verbose_name=u"Ссылка")
    short_urn = models.SlugField(unique=True, default=generateURN, verbose_name=u"Короткая ссылка")
    created_at = models.DateTimeField(default=datetime.datetime.now, help_text=u"Время создания", editable=False)
    conversions = models.IntegerField(default=0, help_text=u"Количество переходов", editable=False)

    class Meta:
        ordering = ('-created_at',)

    def increase_conversions(self):
        self.conversions += 1
        self.save()

    def get_absolute_url(self):
        return self.short_urn