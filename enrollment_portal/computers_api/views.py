from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ComputerProduct
from .serializers import ComputerProductSerializer


class ComputerProductViewSet(viewsets.ModelViewSet):
    serializer_class = ComputerProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ComputerProduct.objects.all()
        category = self.request.query_params.get("category")
        brand = self.request.query_params.get("brand")
        search = self.request.query_params.get("search")

        if category:
            queryset = queryset.filter(category__iexact=category)
        if brand:
            queryset = queryset.filter(brand__iexact=brand)
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(brand__icontains=search)
                | Q(specs__icontains=search)
            )
        return queryset
