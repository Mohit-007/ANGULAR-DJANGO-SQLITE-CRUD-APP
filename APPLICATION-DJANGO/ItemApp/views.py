from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse

from ItemApp.models import Item
from ItemApp.serializers import ItemSerializer

# Create your views here.

@csrf_exempt
def itemApi(request, id=0):
    if request.method == 'GET':
        items = Item.objects.all()
        item_serializer = ItemSerializer(items, many=True)
        return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data = item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("added successfully", safe = False)
        return JsonResponse("failed to add", safe = False)
    if request.method == 'DELETE':
        item = Item.objects.get(ItemId=id)
        item.delete()
        return JsonResponse("deleted sucessfully", safe = False)
    

