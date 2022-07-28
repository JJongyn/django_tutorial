
from dataclasses import field
from pyexpat import model
from .models import Accounts
from rest_framework import serializers

class AccountsSerializer(serializers.ModelSerializer):

    user_pw = serializers.CharField()

    class Meta:
        model = Accounts
        fields = ['user_id', 'user_pw', 'user_email', 'user_name', 'user_created']

