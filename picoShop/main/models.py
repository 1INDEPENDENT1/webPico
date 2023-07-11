from django.db import models
from django.utils.translation import gettext_lazy as _


class Orders(models.Model):
    objects = None
    ORDER_STATUS_CHOICES = (
        ('delivered', _('Доставлен')),
        ('in_progress', _('В работе')),
        ('exception', _('Отменен')),
        ('complete', _('Выполнено'))
    )

    uni_code = models.CharField('Уникальный код', max_length=16)
    log_pass = models.CharField('Логин и пароль', max_length=80)
    order_number = models.CharField('Номер заказа', max_length=10)
    order_date = models.DateTimeField('Дата и время')
    game_name = models.CharField('Название игры', max_length=50)
    status = models.CharField('Статус заказа', max_length=20, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class token_storage(models.Model):
    objects = None

    token = models.CharField('Токен', max_length=64)
    seller_id = models.IntegerField('ID продавца')
    valid_thru = models.IntegerField('Годен до')

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'
