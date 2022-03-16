from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Products
from products import serializers

@api_view(['GET'])
def products_list(request):
    product = Products.objects.all()

    serializer = ProductSerializer(title, many=True)

    return Response(serializer.data)