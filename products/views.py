import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def get_products(request):
    url = "https://amazon-products1.p.rapidapi.com/search"

    querystring = {"country": "US", "query": "MacBook+Pro", "page": "1"}

    headers = {
        'x-rapidapi-host': "amazon-products1.p.rapidapi.com",
        'x-rapidapi-key': "1161cb8e24msh971995c853e2456p137600jsn9dbe458002c2"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = json.loads(response.content)
    return JsonResponse(response_json)
