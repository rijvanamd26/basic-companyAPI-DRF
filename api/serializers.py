from rest_framework import serializers
from api.models import *

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
        read_only_fields = ['company_id']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        read_only_fields = ['id']
        
 