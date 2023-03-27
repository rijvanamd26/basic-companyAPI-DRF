from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #custom fn url = api/v1/companies/id/employees/
    @action(detail=True, methods=['GET'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message' : 'Company might not exist error',
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer