"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver

from boards.models import Label, List
from members.models import Member
from task_management.models import BaseModel


class Card(BaseModel):
    """
    Cards have an order within a list and can be assigned to members, they may have one label
    """
    title = models.CharField(max_length=100, blank=False, null=False)

    description = models.CharField(max_length=255, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    order = models.PositiveIntegerField(blank=False, null=False, default=1)

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    label = models.ForeignKey(Label, null=True, on_delete=models.SET_NULL)

    members = models.ManyToManyField(Member)

    created_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='card_created')
    modified_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='card_modified')

    def __str__(self):
        return '%s - %s' % (self.title, self.description)


@receiver(pre_save, sender=Card)
def reorder_cards(sender, instance, **kwargs):
    """
    Reorder all cards in a list if a card is saved or deleted (archived)
    :param sender: Signal sender (not used)
    :param instance: Actual instance to be saved
    :param kwargs: Dict
    :return: None
    """
    if instance.archived:
        cards_to_reorder = Card.objects.filter(order__gt=instance.order, list=instance.list)
        cards_to_reorder.update(order=F('order') - 1)
    else:
        cards_to_reorder = Card.objects.filter(order__gte=instance.order, list=instance.list)
        cards_to_reorder.update(order=F('order') + 1)
