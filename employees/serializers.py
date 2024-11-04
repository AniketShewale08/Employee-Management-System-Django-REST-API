from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_email(self, value):
        if Employee.objects.filter(email = value).exists():
            raise serializers.ValidationError("This email is already is use.")
        return value
    