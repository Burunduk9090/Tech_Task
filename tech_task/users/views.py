from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Address, CreditCard
from .serializers import UserSerializer, AddressSerializer, CreditCardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_addresses(request):
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_credit_cards(request):
    credit_cards = CreditCard.objects.all()
    serializer = CreditCardSerializer(credit_cards, many=True)
    return Response(serializer.data)
