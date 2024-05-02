from django.urls import path
from .views import *
urlpatterns = [
    path('vendors/', vendors_list_create, name='list_create_vendors'),
    path('vendors/<int:pk>/', vendor_detail, name='detail_update_delete_vendor'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceRetrieveAPIView.as_view(), name='vendor_performance'),
]
