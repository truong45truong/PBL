from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Products, Categories, Sizes, Prices
from .serializers import ProductSerializer
from slugify import slugify
@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET /api/product'
    ]
    return Response(routes)

@api_view(['GET','POST'])
def getAllProduct(request):
    if request.method == 'GET':
        list_item_product= request.GET.get('list_shopping_cart')
        products = Products.objects.all()
        serializers = ProductSerializer(products, many=True) 
        return Response(serializers.data)
def getProduct(request, slug):
    pass
@api_view(['GET','POST'])
def createProduct(request):
    if request.method == 'POST':
        list_item_product= request.GET.get('cart')
        print(list_item_product)
        product = Products(name="truong", sex=1, description="truongdeptrai"
                                       , slug=slugify(
                                           "truong"+"-123" 
                                       ))
        product.save()
        serializers = ProductSerializer(product)
        return Response(serializers.data)
