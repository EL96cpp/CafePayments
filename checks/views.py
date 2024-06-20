from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Check
from customers.models import CustomerCard
from employees.models import Employee
from .serializers import CheckSerializer


class CheckAPIView(APIView):

    def post(self, request):
        customer = request.data['customer']
        employee_id = request.data['employee_id']
        order = dict(request.data['order'])

        print(order)

        if not CustomerCard.objects.filter(email = customer['email']).exists():
            return Response({'post': 'No card in database!'}, status=status.HTTP_404_NOT_FOUND)
        card = CustomerCard.objects.filter(email = customer['email']).first()
        if card.name != customer['name'] or card.surname != customer['surname'] or card.email != customer['email']:
            return Response({'post': 'Invalid customer data!'}, status=status.HTTP_404_NOT_FOUND)
        elif not Employee.objects.filter(pk = employee_id).exists():
            return Response({'post': 'Incorrect employee id!'}, status=status.HTTP_404_NOT_FOUND)
        
        check = Check.objects.create(
            employee = employee_id,
            customer = card.pk,
            discount = card.discount,
            total_no_discount = 0,
            total_with_discount = 0,
            order = {},
            date = ''
        )
        return Response({'post': CheckSerializer(check).data}, status=status.HTTP_201_CREATED)
    
    
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
