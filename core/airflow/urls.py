from django.urls import path, include
from airflow.views import SearchIdView, SearchResultView, SearchDetail


urlpatterns = [
    path('',  SearchIdView.as_view(), name='search-create'),
    path('results/',  SearchResultView.as_view(), name='search-view'),  
    path('results/<str:uuid>/',  SearchDetail.as_view(), name='search-detail'),
]
