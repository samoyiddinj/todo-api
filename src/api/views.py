from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import RemovedInDRF317Warning
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

@api_view(['GET'])
def api_main(*args, **kwargs):
    model_data = Product.objects.all().first()
    data = {}
    # data['id'] = model_data.id
    # data['title'] = model_data.title
    # data['description'] = model_data.description
    # data['price'] = model_data.price
    data = ProductSerializer(model_data).data

    return Response(data)
