from django.contrib import admin
from airflow.models import SearchResult, ExchangeRate


admin.site.register(SearchResult)
admin.site.register(ExchangeRate)
