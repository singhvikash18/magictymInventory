from django.db import models
from django.db.models.fields import Field
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
         model =Customer
         fields ='__all__'
