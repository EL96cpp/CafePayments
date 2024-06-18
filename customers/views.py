from rest_framework.views import APIView
from rest_framework.response import Response
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
        return Response({'post': CustomerCardSerializer(card_new).data})