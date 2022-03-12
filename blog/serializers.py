from rest_framework import serializers
from .models import Products


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
           'image', 'title', 'content', 'timestamp', 'price'
        ]
        read_only_fields = ['name']
