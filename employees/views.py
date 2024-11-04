from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department', lookup_expr='exact')
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')

    class Meta:
        model = Employee
        fields = ['department', 'role'] 


from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter