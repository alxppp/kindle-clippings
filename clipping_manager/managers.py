from random import randint

from django.db import models
from django.db.models import Count


class ClippingQuerySetManager(models.QuerySet):

    def for_user(self, user):
        return self.filter(user=user)

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class BookQuerySetManager(models.QuerySet):

    def for_user(self, user):
        return self.filter(user=user)