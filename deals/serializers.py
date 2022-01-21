from rest_framework import serializers
from deals.models import Inventory, Deals

class InventorySerialzer(serializers.ModelSerializer):

    class Meta:
        name = Inventory
        fields = '__all__'

class DealsSerializer(serializers.ModelSerializer):

    class Meta:
        name = Deals
        fields = '__all__'