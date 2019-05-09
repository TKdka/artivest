'''
Created on May 8, 2019

@author: tom
'''

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from cake import models 
from cake import sers



class CakeViewSet(ModelViewSet):
    
    lookup_field = 'display_name'

    queryset = models.Cake.objects.all()
    serializer_class = sers.CakeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'partial_update':
            return sers.CakePartialUpdateSerializer
        else:
            return sers.CakeSerializer
    