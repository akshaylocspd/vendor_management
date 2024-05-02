from django.contrib import admin
from .models import HistoricalPerformance

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('vendor', 'date')
    search_fields = ['vendor__name']  # Assuming 'name' is a field in the Vendor model

admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
