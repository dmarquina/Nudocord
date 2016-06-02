from deliverplaces.models import Deliverplace

from rest_framework import serializers


class PlacesnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverplace
        fields = ('id', 'name')


class PlacesdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverplace
        fields = ('id', 'date')
