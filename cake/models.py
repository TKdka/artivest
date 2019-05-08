'''
Created on May 7, 2019

@author: tom
'''

from django.db import models 

class StandardModel(models.Model):
    
    id  = models.AutoField(primary_key = True)
    created_timestamp = models.DateTimeField(auto_now_add = True)
    modified_timestamp = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True 
        
class Cake(StandardModel):
    
    display_name = models.CharField(max_length = 255, unique = True)
    candies = models.CharField(max_length = 200)
    max_slices = models.IntegerField()
    number_minions = models.PositiveIntegerField()
    is_valid_cake = models.BooleanField()
    
    class Meta:
        managed = True 