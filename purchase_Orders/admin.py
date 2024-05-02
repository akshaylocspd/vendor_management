from django.contrib import admin
from .models import PurchaseOrder

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'status')
    list_filter = ('vendor', 'status', 'order_date', 'delivery_date')
    search_fields = ('po_number', 'vendor__name')  # Assuming Vendor has a 'name' field
    date_hierarchy = 'order_date'
    readonly_fields = ('issue_date', 'acknowledgment_date')
