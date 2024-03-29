from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)
    

    def post(self,request):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is created'})
        return Response({'Failed':'Product is not created'})
    