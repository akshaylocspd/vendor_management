from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from accounts.models import *
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView


class CustomResponseMixin:
    def get_response_data(self, status, message, data=None):
        return {
            "status": status,
            "message": message,
            "data": data
        }

class PurchaseOrderListCreateAPIView(CustomResponseMixin, ListCreateAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(self.get_response_data(True, "Purchase order created successfully", serializer.data),
                            status=status.HTTP_201_CREATED, headers=headers)
        return Response(self.get_response_data(False, "Failed to create purchase order", serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Get vendor_id from query parameters
        vendor_id = request.query_params.get('vendor_id')

        if vendor_id:
            # Filter queryset by vendor_id
            queryset = queryset.filter(vendor_id=vendor_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.get_response_data(True, "Purchase orders list retrieved successfully", serializer.data))


class PurchaseOrderRetrieveUpdateDestroyAPIView(CustomResponseMixin, RetrieveUpdateDestroyAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(self.get_response_data(True, "Purchase order updated successfully", serializer.data))
        return Response(self.get_response_data(False, "Failed to update purchase order", serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(self.get_response_data(True, "Purchase order deleted successfully"),
                        status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(self.get_response_data(True, "Purchase order details retrieved successfully", serializer.data))


class PurchaseOrderAcknowledgeAPIView(RetrieveUpdateAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save()
        avg_time=instance.vendor.calculate_average_response_time()
        return Response({'message': 'Purchase order acknowledged successfully',"average_response_time":avg_time}, status=status.HTTP_200_OK)
