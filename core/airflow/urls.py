from django.urls import path, include
from airflow.views import SearchResultView


urlpatterns = [
    path('',  SearchResultView.as_view(), name='search-create'),
]
