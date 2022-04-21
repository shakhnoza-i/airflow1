from django.urls import path, include
from airflow.views import SearchIdView, SearchResultView, SearchDetail, ExchangeRateView


urlpatterns = [
    path('',  SearchIdView.as_view(), name='search-create'),
    path('results/',  SearchResultView.as_view(), name='search-view'),  
    path('results/<str:uuid>/<str:currency>/',  SearchDetail.as_view(), name='search-detail'),
    path('currency/',  ExchangeRateView.as_view(), name='exchange-view'),
]
