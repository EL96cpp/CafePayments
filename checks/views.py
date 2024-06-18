from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
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
            return Response({'post': 'No card in database!'})
        card = CustomerCard.objects.filter(email = customer['email']).first()
        if card.name != customer['name'] or card.surname != customer['surname'] or card.email != customer['email']:
            return Response({'post': 'Invalid customer data!'})
        elif not Employee.objects.filter(pk = employee_id).exists():
            return Response({'post': 'Incorrect employee id!'})
        
        discount = card.discount
        print(discount)


        return Response({'post': 'ok'})
    
    permission_classes = (IsAuthenticated, )