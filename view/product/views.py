from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product


class ProductView(View):
    def get(self, request):
        return render(request, 'task/product/product.html')

class ProductViewAPI(APIView):
    def get(self,request):
        data = Product.objects.all().values()
        return Response(data)