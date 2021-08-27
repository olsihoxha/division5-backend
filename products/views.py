import json

import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from common.models import UserData
from products.serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
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
    serializer_class = ProductSerializer

    def get_queryset(self):
        return UserData.objects.first().first()
