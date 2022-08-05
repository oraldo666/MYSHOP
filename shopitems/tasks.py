from __future__ import unicode_literals, absolute_import

from celery import shared_task
from .models import ItemModel


@shared_task
def test_function():
    # operations
    first_model = ItemModel.objects.get(pk=1)
    print(first_model.title)
    return 'Done'


@shared_task
def add_num(a, b):
    print(a + b)
    return 'Done'
