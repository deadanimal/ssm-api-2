from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    Transaction,

)

from carts.serializers import CartSerializer

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionWithCartSerializer(serializers.ModelSerializer):

    cart = CartSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'