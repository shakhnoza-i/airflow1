from rest_framework import serializers
from airflow.models import SearchResult, ExchangeRate
from airflow.tasks import CurrencyRate
from django.db.models import Case, When, F


class SearchIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = ['search_id']


class SearchOrderSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('calculate_price')
    currency = serializers.SerializerMethodField('get_currency')

    def get_currency(self, search_result):
        return 'KZT'

    def calculate_price(self, search_result):
        rate = CurrencyRate()
        currency_rate = rate.curr
        price = SearchResult.objects.filter(search_id=search_result.search_id).annotate(price_kzt = Case(
        When(currency="EUR", then=F('price') * currency_rate ),
            # Assumes that the only other currency is KZT
            default=F('price')
        )).first()
        price_kzt = price.price_kzt if price else 0
        # breakpoint()
        return price_kzt
    
    class Meta:
        model = SearchResult
        fields = ['search_id', 'price', 'currency', 'items']


class SearchOrderEURSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('calculate_price')
    currency = serializers.SerializerMethodField('get_currency')

    def get_currency(self, search_result):
        return 'EUR'

    def calculate_price(self, search_result):
        rate = CurrencyRate()
        currency_rate = rate.curr
        price = SearchResult.objects.filter(search_id=search_result.search_id).annotate(price_kzt = Case(
        When(currency="KZT", then=F('price') / currency_rate ),
            # Assumes that the only other currency is KZT
            default=F('price')
        )).first()
        price_kzt = price.price_kzt if price else 0
        # breakpoint()
        return price_kzt
    
    class Meta:
        model = SearchResult
        fields = ['search_id', 'price', 'currency', 'items']


class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'
