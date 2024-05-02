from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import *
from .models import *
from .serializers import *

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, fatmug.<br> this project is developed by <h2>Akshay Vijay Vairagade</h2>")

class CustomResponseMixin:
    def get_response_data(self, status, message, data=None):
        return {
            "status": status,
            "message": message,
            "data": data
        }
    
# if you want to apply authentication to only GET Api 
# solution is to create different endpoint in urls.py
@api_view(['GET', 'POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])       
def vendors_list_create(request):
    if request.method == 'GET':
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)
        # return Response(serializer.data)
        return Response(CustomResponseMixin().get_response_data(status=True, message="Vendors list", data=serializer.data), status=status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'userData':VendorSerializer(user).data
            }
            return Response(CustomResponseMixin().get_response_data(status=True, message="Vendor created successfully", data=response_data), status=status.HTTP_201_CREATED)
        return Response(CustomResponseMixin().get_response_data(status=False, message="Failed to create vendor", data=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def vendor_detail(request, pk):    
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response(CustomResponseMixin().get_response_data(status=False, message="Vendor not found"), status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(CustomResponseMixin().get_response_data(status=True, message="Vendor retrieved successfully", data=serializer.data))
    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CustomResponseMixin().get_response_data(status=True, message="Vendor updated successfully", data=serializer.data))
        return Response(CustomResponseMixin().get_response_data(status=False, message="Failed to update vendor", data=serializer.errors), status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vendor.delete()
        return Response(CustomResponseMixin().get_response_data(status=True, message="Vendor deleted successfully"))

class VendorPerformanceRetrieveAPIView(RetrieveAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            'on_time_delivery_rate': instance.calculate_on_time_delivery_rate(),
            'quality_rating_avg': instance.calculate_quality_rating_avg(),
            'average_response_time': instance.calculate_average_response_time(),
            'fulfillment_rate': instance.calculate_fulfillment_rate()
        }
        serializer = self.get_serializer(data)
        return Response(serializer.data)
