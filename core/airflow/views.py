import random
import requests
import uuid
from django.db.models import Case, When, F
from rest_framework import generics
from rest_framework.response import Response

from airflow.models import SearchResult
from airflow.serializers import SearchOrderSerializer, SearchResultSerializer, SearchIdSerializer
from airflow.tasks import CurrencyRate


def random_service():
    services = [1,1,1,1,1,2]
    service = random.choice(services)
    return service


class SearchIdView(generics.CreateAPIView):
    serializer_class = SearchIdSerializer

    def create(request, exchange_rate, *args, **kwargs):
        a_b = random_service()
        if a_b ==1:
            req1 = requests.post('http://127.0.0.1:8990/search')
            all_flights = req1.json()
        else:
            req1 = requests.post('http://127.0.0.1:8991/search')
            all_flights = req1.json()

        flight_id = random.randrange(len(all_flights))
        flight = all_flights[flight_id]
        search_id = str(uuid.uuid4())
        price = flight.get('pricing').get('total')
        currency = flight.get('pricing').get('currency')

        search_result = SearchResult.objects.create(
            search_id = search_id,
            price = price,
            currency = currency,
            status = 'completed',
            items = flight
        )
        search_result.save()

        return Response({"search_id": search_id})


class SearchResultView(generics.ListAPIView):
    """View all searches ordering by price"""
    serializer_class = SearchOrderSerializer
    queryset = SearchResult.objects.all().order_by('price')


class SearchDetail(generics.RetrieveAPIView):

    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer
