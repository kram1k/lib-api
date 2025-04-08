from textwrap import shorten

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from .constansts import (
    MAX_NAME_LEN,
    MAX_FIELD_LEN,
    SHORT_NAME_LEN,
    MAX_YEAR,
    MIN_YEAR
)


class Library(models.Model):
    """
    Модель, представляющая библиотеку.

    Содержит основную информацию о библиотеке, включая её название, регион, адрес,
    год основания и размер межбюджетного трансферта.
    """
    full_name = models.CharField(_("Учреждение"), max_length=MAX_NAME_LEN)
    region = models.CharField(_("Регион"), max_length=MAX_FIELD_LEN)
    address = models.CharField(_("Адрес"), max_length=MAX_FIELD_LEN)
    year = models.IntegerField(
        _("Год"),
        validators=[
            MinValueValidator(MIN_YEAR),
            MaxValueValidator(MAX_YEAR)]
    )
    inter_budget_transfer_amount = models.IntegerField(
        _("Размер иного межбюджетного трансферта руб")
    )

    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"

    def __str__(self):
        return shorten(
            self.full_name,
            width=SHORT_NAME_LEN,
            placeholder=" ..."
        )
