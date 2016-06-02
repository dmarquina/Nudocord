import json

from deliverplaces.models import Deliverplace

from .serializers import PlacesnameSerializer
from .serializers import PlacesdateSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', ])
def api_deliverplacesname(request):
    deliverplaces = Deliverplace.objects.order_by('name').distinct('name')
    serializer = PlacesnameSerializer(deliverplaces, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def api_deliverplacesdate(request, pk):
    deliverplace = Deliverplace.objects.get(pk=pk)
    deliverplaces = Deliverplace.objects.filter(name=deliverplace.name)
    serializer = PlacesdateSerializer(deliverplaces, many=True)
    return Response(serializer.data)

