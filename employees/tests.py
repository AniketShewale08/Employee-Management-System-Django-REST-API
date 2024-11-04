from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from employees.models import Employee
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.employee_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'Engineering',
            'role': 'Developer'
        }
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_create_employee(self):
        url = reverse('employee-list')
        response = self.client.post(url, self.employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().name, 'John Doe')

    def test_get_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_update_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        url = reverse('employee-detail', args=[employee.id])
        updated_data = {'name': 'Jane Doe', 'email': 'janedoe@example.com'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Doe')

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_create_employee_with_duplicate_email(self):
        Employee.objects.create(**self.employee_data)
        url = reverse('employee-list')
        response = self.client.post(url, self.employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
