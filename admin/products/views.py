

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response 



from .models import Product

from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):    # /api/products  get request
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def create(self, request):  # /api/product post request
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):    # api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def update(self, request):
        pass


    def destroy(self, request):
        pass