from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_email(self, value):
        """
        Validate that the email is unique and has a proper format.
        """
        if self.instance and self.instance.email == value:
            # Allow updates if the email is unchanged
            return value
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_name(self, value):
        """
        Validate that the name field is not empty and does not contain only spaces.
        """
        if not value.strip():
            raise serializers.ValidationError("Name field cannot be empty.")
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value

    def validate_department(self, value):
        """
        Validate that the department is not empty if provided.
        """
        if value and not value.strip():
            raise serializers.ValidationError("Department field cannot be blank.")
        return value

    def validate_role(self, value):
        """
        Validate that the role is not empty if provided.
        """
        if value and not value.strip():
            raise serializers.ValidationError("Role field cannot be blank.")
        return value
