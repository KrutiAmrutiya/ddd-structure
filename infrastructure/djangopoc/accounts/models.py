from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import GENDER_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    phone_number = PhoneNumberField(
        blank=True,
        unique=False,
        null=True,
          )
    gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=10)
    date_of_birth = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        """ String representation of user """
        return self.username
