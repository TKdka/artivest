'''
Created on May 8, 2019

@author: tom
'''

from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from cake import models 
from cake import sers

class CakeViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    
    lookup_field = 'display_name'
    queryset = models.Cake.objects.all()
    serializer_class = sers.CakeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'partial_update':
            return sers.CakePartialUpdateSerializer
        else:
            return sers.CakeSerializer
    