import uuid

from django.db import models


class SearchResult(models.Model):
    search_id = models.UUIDField(default=uuid.uuid4, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(default='KZT', max_length=10)
    status = models.CharField(max_length=20)
    items = models.JSONField()

    def __str__(self): 
        return self.search_id