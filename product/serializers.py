from rest_framework import serializers
from .models import Category, Product, Review, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'tags']

    def validate(self, data):
        tags = data.get('tags')
        if tags:
            for tag in tags:
                if not Tag.objects.filter(name=tag['name']).exists():
                    raise serializers.ValidationError(f"Тег {tag['name']} не существует в базе данных.")
        return data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'product', 'stars']
