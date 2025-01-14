from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items,many=True)
    person = {'name':'Dennis', 'age':28}
    return Response(serializer.data)