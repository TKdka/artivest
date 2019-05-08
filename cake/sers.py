'''
Created on May 8, 2019

@author: tom
'''
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers

from cake import models
from cake.rules import CandiesFormatVaildator, EqualSequenceSlicer
from wsgiref import validate

class CakeSerializer(ModelSerializer):
    #NB: Tricky part is that is_valid_cake, max_slices, number_minions are null in the input
    #but required in the model.  Hence, the extra kwargs
    
    def create(self, validated_data):
        import pdb 
        pdb.set_trace()
        max_slices = EqualSequenceSlicer().get_max_slices(validated_data['candies'])
        num_minions = validated_data['number_minions']   
             
        validated_data['max_slices'] = max_slices
        validated_data['is_valid_cake'] = num_minions <= max_slices
        return ModelSerializer.create(self, validated_data)

    class Meta:
        model = models.Cake 
        exclude = ['created_timestamp', 'modified_timestamp']
        extra_kwargs = {'is_valid_cake': {'required': False},
                        'max_slices': {'required': False},
                        }
        