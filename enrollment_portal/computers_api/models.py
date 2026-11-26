from django.db import models


class ComputerProduct(models.Model):
    CATEGORY_CHOICES = [
        ("Laptop", "Laptop"),
        ("Desktop PC", "Desktop PC"),
        ("Processor", "Processor (CPU)"),
        ("Graphics Card", "Graphics Card (GPU)"),
        ("Motherboard", "Motherboard"),
        ("Memory", "Memory (RAM)"),
        ("Storage", "Storage (SSD/NVMe)"),
        ("Monitor", "Monitor"),
        ("Peripheral", "Peripheral"),
    ]

    sku = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=60)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    specs = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.brand} {self.name} ({self.category})"
