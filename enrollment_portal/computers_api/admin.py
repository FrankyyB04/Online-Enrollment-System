from django.contrib import admin
from .models import ComputerProduct


@admin.register(ComputerProduct)
class ComputerProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "brand", "category", "price", "stock", "is_available")
    list_filter = ("category", "brand", "is_available")
    search_fields = ("sku", "name", "brand", "specs")
