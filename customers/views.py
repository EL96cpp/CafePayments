from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import CustomerCard
from .serializers import CustomerCardSerializer


class CustomerCardAPIView(APIView):

    def post(self, request):
        email = request.data['email']
        if CustomerCard.objects.filter(email=email).exists():
            return Response({'post': 'error!!'})

        card_new = CustomerCard.objects.create(
            name = request.data['name'],
            surname = request.data['surname'],
            email = request.data['email'],
            total_spent = 0,
            discount = 0
        )
        return Response({'post': CustomerCardSerializer(card_new).data}, status=status.HTTP_201_CREATED)


    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
