'''
Created on May 8, 2019

@author: tom
'''

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from cake import models 
from cake import sers

class CakeViewSet(ModelViewSet):
    
    queryset = models.Cake.objects.all()
    serializer_class = sers.CakeSerializer
    permission_classes = [permissions.AllowAny]
    
    