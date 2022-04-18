from rest_framework import serializers
from airflow.models import SearchResult


class SearchResultSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SearchResult
        # fields = "__all__"
        exclude = ['id']



class SearchIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResult
        fields = ['search_id']
