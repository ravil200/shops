from django.contrib import admin
from sale.models import Order, OrderLine

@admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'get_cost'
    )
@admin.site.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'address',
        'order_status',
        'get_total_cost'
    )