from django.shortcuts import render
from rest_framework.views import APIView
from demoapp.serializers import EmployeeSerializer
from demoapp.models import Employee
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import ListAPIView, DestroyAPIView
# Create your views here.




class EmployeeListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeRetrieveUpdateDestroyModelMixin(mixins.UpdateModelMixin,DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
