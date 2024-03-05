from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)
    

    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is created'})
        return Response({'Failed':'Product is not created'})
    


    def put(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})
    


    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductSerializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})

    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'deletion':'Data is Deleted'})