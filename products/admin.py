from django.contrib import admin
from .models import Order, OrderItem, Category, Product



class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(Category)