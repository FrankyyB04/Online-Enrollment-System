from decimal import Decimal
from django.core.management.base import BaseCommand
from computers_api.models import ComputerProduct


SAMPLE_COMPUTERS = [
    ("CMP-001", "ROG Strix G16", "ASUS", "Laptop", "Intel Core i7-13650HX, 16GB DDR5, 1TB NVMe, RTX 4060 8GB, 16-inch FHD 165Hz", "78995.00", 8),
    ("CMP-002", "Legion Slim 5 Gen 9", "Lenovo", "Laptop", "AMD Ryzen 7 8845HS, 16GB DDR5, 1TB SSD, RTX 4060 8GB, 16-inch WQXGA 165Hz", "82495.00", 6),
    ("CMP-003", "MacBook Air 13 M3", "Apple", "Laptop", "Apple M3 8-Core CPU, 10-Core GPU, 16GB Unified Memory, 512GB SSD", "74990.00", 12),
    ("CMP-004", "Nitro V 15", "Acer", "Laptop", "Intel Core i5-13420H, 16GB DDR5, 512GB NVMe, RTX 4050 6GB, 15.6-inch 144Hz", "49995.00", 15),
    ("CMP-005", "ThinkPad X1 Carbon Gen 12", "Lenovo", "Laptop", "Intel Core Ultra 7 155U, 32GB LPDDR5x, 1TB Gen4 SSD, 14-inch WUXGA IPS", "104500.00", 4),
    ("CMP-006", "Predator Orion 3000", "Acer", "Desktop PC", "Intel Core i7-14700F, 32GB DDR5, 1TB NVMe + 2TB HDD, RTX 4070 12GB", "96995.00", 5),
    ("CMP-007", "MAG Infinite S3", "MSI", "Desktop PC", "Intel Core i5-14400F, 16GB DDR5, 1TB NVMe SSD, RTX 4060 Ti 8GB", "64995.00", 7),
    ("CMP-008", "Ryzen 7 7800X3D", "AMD", "Processor", "8 Cores, 16 Threads, 4.2GHz Base / 5.0GHz Boost, 96MB 3D V-Cache, AM5", "24850.00", 14),
    ("CMP-009", "Ryzen 5 5600", "AMD", "Processor", "6 Cores, 12 Threads, 3.5GHz Base / 4.4GHz Boost, 35MB Cache, AM4", "6795.00", 25),
    ("CMP-010", "Core i5-14600K", "Intel", "Processor", "14 Cores (6P+8E), 20 Threads, up to 5.3GHz, LGA1700, Integrated UHD 770", "18950.00", 11),
    ("CMP-011", "GeForce RTX 4070 Super Dual", "ASUS", "Graphics Card", "12GB GDDR6X, 192-bit, DLSS 3.5, Dual Axial-Tech Fans, PCIe 4.0", "38995.00", 9),
    ("CMP-012", "Radeon RX 7800 XT Challenger", "ASRock", "Graphics Card", "16GB GDDR6, 256-bit, Dual Fan Cooling, DisplayPort 2.1 / HDMI 2.1", "31495.00", 10),
    ("CMP-013", "GeForce RTX 4060 Ventus 2X", "MSI", "Graphics Card", "8GB GDDR6, 128-bit, Twin Frozr Thermal Design, PCIe 4.0", "18995.00", 18),
    ("CMP-014", "MAG B650 Tomahawk WiFi", "MSI", "Motherboard", "AMD AM5 ATX, DDR5 up to 7600+ MHz, PCIe 4.0, Triple M.2, Wi-Fi 6E", "13450.00", 13),
    ("CMP-015", "B550M Pro4 Micro-ATX", "ASRock", "Motherboard", "AMD AM4 mATX, DDR4 up to 4733+ MHz, Dual M.2, 2.5G LAN", "5895.00", 20),
    ("CMP-016", "Vengeance RGB 32GB (2x16GB) DDR5", "Corsair", "Memory", "6000MHz CL30, Intel XMP 3.0 & AMD EXPO Ready, Black Heatspreader", "7650.00", 22),
    ("CMP-017", "Ripjaws V 16GB (2x8GB) DDR4", "G.Skill", "Memory", "3200MHz CL16, 1.35V Dual Channel Desktop Memory Kit", "2395.00", 30),
    ("CMP-018", "990 PRO 2TB PCIe 4.0 NVMe", "Samsung", "Storage", "M.2 2280 SSD, Sequential Read up to 7,450 MB/s, Write up to 6,900 MB/s", "10950.00", 16),
    ("CMP-019", "KC3000 1TB PCIe 4.0 NVMe", "Kingston", "Storage", "M.2 2280 SSD, 3D TLC NAND, Graphene Aluminum Heat Spreader, 7,000 MB/s", "5295.00", 24),
    ("CMP-020", "UltraGear 27GP850-B", "LG", "Monitor", "27-inch QHD (2560x1440) Nano IPS, 165Hz (OC 180Hz), 1ms GtG, G-Sync Compatible", "19495.00", 9),
    ("CMP-021", "G24F 2 Gaming Monitor", "Gigabyte", "Monitor", "23.8-inch FHD (1920x1080) SS IPS, 165Hz (OC 180Hz), 1ms MPRT, 95% DCI-P3", "8995.00", 17),
    ("CMP-022", "Keychron K2 Pro Mechanical Keyboard", "Keychron", "Peripheral", "75% Layout, Hot-Swappable Gateron Red Switches, QMK/VIA, Bluetooth & USB-C", "5490.00", 14),
    ("CMP-023", "G Pro X Superlight 2", "Logitech", "Peripheral", "60g Wireless Gaming Mouse, HERO 2 Sensor 32K DPI, LIGHTSPEED Wireless", "8295.00", 11),
    ("CMP-024", "MX Master 3S Wireless Mouse", "Logitech", "Peripheral", "8K DPI Darkfield Sensor, Quiet Clicks, MagSpeed Electromagnetic Wheel, USB-C", "5795.00", 19),
]


class Command(BaseCommand):
    help = "Seeds the database with 24 computer e-commerce products."

    def handle(self, *args, **options):
        created_count = 0
        for sku, name, brand, category, specs, price, stock in SAMPLE_COMPUTERS:
            _, created = ComputerProduct.objects.get_or_create(
                sku=sku,
                defaults={
                    "name": name,
                    "brand": brand,
                    "category": category,
                    "specs": specs,
                    "price": Decimal(price),
                    "stock": stock,
                    "is_available": True,
                },
            )
            if created:
                created_count += 1

        total = ComputerProduct.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Seeding complete: {created_count} new products added ({total} total in database)."
            )
        )
