from django.db import models
from django.core import validators
from django.core.validators import *


class ContactForm(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(1)])
    email = models.EmailField(validators=[validators.validate_email])
    phone = models.CharField(max_length=10)
    message = models.TextField(validators=[validators.MaxLengthValidator(500)])

    def __str__(self):
        return self.name


