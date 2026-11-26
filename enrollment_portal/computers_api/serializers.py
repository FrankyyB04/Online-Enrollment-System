from rest_framework import serializers
from .models import ComputerProduct


class ComputerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerProduct
        fields = [
            "id",
            "sku",
            "name",
            "brand",
            "category",
            "specs",
            "price",
            "stock",
            "is_available",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
