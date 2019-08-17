from django.db import models


class Student (models.Model):
    SEX_ITEMS = [
        (0, 'unknow'),
        (1, 'man'),
        (2, 'woman'),
    ]
    STATUS_ITEM = [
        (0, 'application'),
        (1, 'pass'),
        (2, 'refuse'),
    ]
    name = models.CharField(max_length=128, verbose_name='name')

