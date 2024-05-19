from django.db import models
from django.db.models import UniqueConstraint
from djmoney.models.fields import MoneyField


class Debt(models.Model):
    class Types(models.TextChoices):
        ELECTRICITY = 'electricity', 'Электроснабжение'
        GAS = 'gas', 'Газоснабжение'
        WATER = 'water', 'Водоснабжение'

    account = models.CharField("Лицевой счет", max_length=12)
    type = models.CharField("Тип лицевого счета", choices=Types.choices, max_length=12)
    amount = MoneyField('Сумма задолженности', max_digits=14)
    is_paid = models.BooleanField("Оплачено", default=False)

    class Meta:
        verbose_name = "Задолженность"
        verbose_name_plural = "Задолженности"
        constraints = [UniqueConstraint(fields=['type', 'account'], name='unique_account_per_type')]

    def __str__(self):
        return f"Лицевой счет {self.account}"
