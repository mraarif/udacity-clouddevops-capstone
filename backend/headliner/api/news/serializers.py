from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        instance, _ = Article.objects.get_or_create(**validated_data)
        return instance
