from django.db import models
from django.contrib import admin
from .models import category, customer, orders, product

admin.site.register(orders)
admin.site.register(category)
admin.site.register(customer)
admin.site.register(product)