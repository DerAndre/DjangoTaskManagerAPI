"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from django.contrib.auth.models import User
from django.db import models

from task_management.models import BaseModel


class Member(BaseModel):
    """
    Member model with reference to django auth user, providing all attributes and more to fulfill the requirements
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s - %s' % (self.user.first_name, self.user.last_name, self.created_at)
