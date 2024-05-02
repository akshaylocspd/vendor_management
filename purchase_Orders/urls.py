from django.urls import path
from .views import *

urlpatterns = [
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase_order_list_create'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase_order_detail'),
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgeAPIView.as_view(), name='purchase_order_acknowledge'),
]
