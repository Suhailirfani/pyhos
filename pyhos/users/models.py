# Create your models here.
# Create your models here.
# users/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('office_admin', 'Office Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username