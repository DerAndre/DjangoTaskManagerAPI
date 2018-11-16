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

from members.models import Member
from task_management.models import BaseModel


class Board(BaseModel):
    """
    Represents a board which can contain lists and cards
    """
    name = models.CharField(max_length=100, blank=False, null=False)

    created_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='board_created')
    modified_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='board_modified')

    def __str__(self):
        return '%s - %s' % (self.name, self.created_at)


class List(BaseModel):
    """
    Lists contain cards and have an order within a board
    """
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')

    order = models.PositiveIntegerField(blank=False, null=False, default=1)

    created_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='list_created')
    modified_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='list_modified')

    def __str__(self):
        return '%s - %s' % (self.board, self.created_at)


class Label(BaseModel):
    """
    Labels belong to a board (max 6)
    """
    text = models.CharField(max_length=100, blank=False, null=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    created_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='label_created')
    modified_by = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL, related_name='modified_modified')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Override save to make sure that there are not more than 6 labels in a board
        :param force_insert: Not used
        :param force_update: Not used
        :param using: Not used
        :param update_fields: Not used
        :return: Label
        """
        if self.board.label_set.all().count() == 6:
            return
        return super(Label, self).save()

    def __str__(self):
        return '%s - %s' % (self.text, self.created_at)


@receiver(pre_save, sender=List)
def reorder_lists(sender, instance, **kwargs):
    """
    Reorder all lists in a specific board when a list is saved or deleted (archived)
    :param sender: Signal sender (not used)
    :param instance: The actual instance to be saved
    :param kwargs: Dict
    :return: None
    """
    if instance.archived:
        lists_to_reorder = List.objects.filter(order__gt=instance.order, board=instance.board)
        lists_to_reorder.update(order=F('order') - 1)
    else:
        lists_to_reorder = List.objects.filter(order__gte=instance.order, board=instance.board)
        lists_to_reorder.update(order=F('order') + 1)
