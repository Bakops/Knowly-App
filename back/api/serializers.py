from rest_framework import serializers
from base.models import Item

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        modem = Item
        fields = '__all__'