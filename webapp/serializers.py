from rest_framework import serializers
from .models import UserExcuse

class UserExcuseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExcuse
        fields = ['excuse_category', 'excuse', 'excuse_id', 'time_created', 'date_created']