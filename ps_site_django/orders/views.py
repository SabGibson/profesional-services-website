from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import Http404

from rest_framework import status,authentication,permissions
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order,OrderItem
from .serializers import OrderSerializer,MyOrderSerializer
# Create your views here.


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_value = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])


        try:
            charge = stripe.Charge.create(
                amount=int(paid_value*100),
                currency='GBP',
                description="Grünluft",
                source = serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_value=paid_value)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        except:
            return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes= [permissions.IsAuthenticated] 

    def get(self,request,format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders,many=True)
        return Response(serializer.data)