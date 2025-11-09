############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################



Product.objects.all().delete()
print("Cleared old product entries.\n")


products = [
    {"upc": "1111", "name": "Milk", "price": 3.49},
    {"upc": "2222", "name": "Bread", "price": 2.19},
    {"upc": "3333", "name": "Eggs", "price": 4.79},
    {"upc": "4444", "name": "Cheese", "price": 6.25},
    {"upc": "5555", "name": "Butter", "price": 5.10},
]

for item in products:
    Product.objects.create(**item)

print("Added sample products successfully.\n")


print("Current Products in Database:")
for p in Product.objects.all():
    print(f"UPC: {p.upc} | {p.name} - ${p.price}")


print("\nSimulate a product scan:")
user_upc = input("Enter a UPC code to scan: ")

product = Product.objects.filter(upc=user_upc).first()

if product:
    print(f"\nProduct found: {product.name} - ${product.price}")
else:
    print("\nProduct not found in the database.")