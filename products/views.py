from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Products
from products import serializers

@api_view(['GET','POST'])
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = Products.Serializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer == Products.Serializer(data=request.data)
        serializer.is_valid() == True
        serializer.save()
        return Response(serializer.data)

    else:
        return Response(serializer.errors)