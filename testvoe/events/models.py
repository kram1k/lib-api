from textwrap import shorten

from django.db import models
from django.utils.translation import gettext_lazy as _


class Library(models.Model):
    full_name = models.CharField(_("Учреждение"), max_length=50)
    region = models.CharField(_("Учреждение"), max_length=50)
    address = models.CharField(_("Адрес"), max_length=50)
    address = models.CharField(_("Адрес"), max_length=50)
    year = models.IntegerField(min_value=1000, max_value=2100)
    inter_budget_transfer_amount = models.IntegerField(
        _("Размер иного межбюджетного трансферта руб")
    )

    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"

    def __str__(self):
        return shorten(self.name, width=40, placeholder=" ...")
