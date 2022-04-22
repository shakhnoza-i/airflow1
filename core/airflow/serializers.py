from datetime import datetime
from rest_framework import serializers
from django.db.models import Case, When, F
from airflow.models import SearchResult, ExchangeRate
from airflow.tasks import currency_rate


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
        date = datetime.today().strftime('%Y-%m-%d')
        currency_rate = ExchangeRate.objects.filter(date=date).first().rate
        price = SearchResult.objects.filter(search_id=search_result.search_id).annotate(price_kzt = Case(
        When(currency="EUR", then=F('price') * int(currency_rate)),
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
        date = datetime.today().strftime('%Y-%m-%d')
        currency_rate = ExchangeRate.objects.filter(date=date).first().rate
        price = SearchResult.objects.filter(search_id=search_result.search_id).annotate(price_kzt = Case(
        When(currency="KZT", then=F('price') / currency_rate ),
            # Assumes that the only other currency is EUR
            default=F('price')
        )).first()
        price_kzt = price.price_kzt if price else 0
        return price_kzt
    
    class Meta:
        model = SearchResult
        fields = ['search_id', 'price', 'currency', 'items']


class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'
