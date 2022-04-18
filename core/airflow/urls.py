from django.urls import path, include
from airflow.views import SearchIdView, SearchResultView


urlpatterns = [
    path('',  SearchIdView.as_view(), name='search-create'),
    path('results/',  SearchResultView.as_view(), name='search-view'),  
]
