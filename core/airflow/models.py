from turtle import mode
import uuid

from django.db import models


class SearchResult(models.Model):
    search_id = models.UUIDField(default=uuid.uuid4, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    currency = models.CharField(default='KZT', max_length=10)
    status = models.CharField(max_length=20)
    items = models.JSONField()

    def __str__(self): 
        return str(self.search_id)


class Currency(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
