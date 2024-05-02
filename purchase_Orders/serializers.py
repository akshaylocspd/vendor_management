from rest_framework import serializers

from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderAcknowledgeSerializer(serializers.Serializer):
    acknowledgment_date = serializers.DateTimeField()
