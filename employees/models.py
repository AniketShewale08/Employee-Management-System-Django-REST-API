from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Model-level validation for Employee.
        """
        if self.name and not self.name.strip():
            raise ValidationError(_('Name cannot be empty or spaces only.'))
        if self.department and not self.department.strip():
            raise ValidationError(_('Department cannot be blank or spaces only.'))
        if self.role and not self.role.strip():
            raise ValidationError(_('Role cannot be blank or spaces only.'))

    def save(self, *args, **kwargs):
        """
        Call full_clean() before saving to enforce validation rules.
        """
        self.full_clean()
        super().save(*args, **kwargs)
