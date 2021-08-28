import json

import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from products.filters import ProductsFilter
from products.models import Product, SavedProducts
from products.serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
    """
    This function get data from amazon(Rapid-API is the provider),
    it is not as an endpoint on front-end because it has limited requests per month with the basic plan,
    but it wold have worked the same as the endpoint I made with DRF,
    with super small differences like field names
    """
    url = "https://amazon-products1.p.rapidapi.com/search"
    params = request.query_params
    querystring = {"keyword": "iphone", "country": "US", "category": "aps"}
    page = params.get('page', None)
    search_product = params.get('keyword', None)
    if page:
        querystring['page'] = page
    if search_product:
        querystring['keyword'] = search_product

    headers = {
        'x-rapidapi-host': "amazon-products1.p.rapidapi.com",
        'x-rapidapi-key': "1161cb8e24msh971995c853e2456p137600jsn9dbe458002c2"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.content)
    return JsonResponse(response_json)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductsFilter


class ProductSavedListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    filterset_class = ProductsFilter

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(saved_products__user=user).distinct()


@api_view(['POST'])
def save_product(request):
    product_id = request.data.get('product_id')
    if product_id:
        if SavedProducts.objects.filter(user=request.user, product_id=product_id).exists():
            SavedProducts.objects.filter(user=request.user, product_id=product_id).delete()
            return JsonResponse({'response': 'U fshi me sukses'})
        SavedProducts.objects.create(user=request.user, product_id=product_id)
        return JsonResponse({'response': 'U ruajt me sukses'})
    return JsonResponse({'error': 'Te dhena jo te plota'}, status=400)
