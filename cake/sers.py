'''
Created on May 8, 2019

@author: tom
'''
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from cake import models
from cake.rules import CandiesFormatVaildator, EqualSequenceSlicer, CakeValidator


#Need this to ensure is_valid_cake or max_slices  yields a 400 error
#https://github.com/encode/django-rest-framework/issues/1655
class CakePartialUpdateSerializer(ModelSerializer):

    def update(self, instance, validated_data):
        instance = ModelSerializer.update(self, instance, validated_data)
        instance.max_slices = EqualSequenceSlicer().get_max_slices(instance.candies)
        instance.is_valid_cake = CakeValidator().is_valid(instance)  
        instance.save()
        return instance
    
    def validate_candies(self, value):
        if not CandiesFormatVaildator().is_valid(value):
            raise serializers.ValidationError("Candies must be all lower case letters")
        return value
    
    def validate_is_valid_cake(self, value):
        if value != None:
            raise serializers.ValidationError("is_valid_cake is not allowed in partial update")

    def validate_max_slices(self, value):
        if value != None:
            raise serializers.ValidationError("max_slices is not allowed in partial update")

    class Meta:
        model = models.Cake 
        exclude = ['created_timestamp', 'modified_timestamp']


class CakeSerializer(ModelSerializer):
    
    def validate_candies(self, value):
        if not CandiesFormatVaildator().is_valid(value):
            raise serializers.ValidationError("Candies must be all lower case letters")
        return value
    
    def create(self, validated_data):
        
        max_slices = EqualSequenceSlicer().get_max_slices(validated_data['candies'])
        validated_data['max_slices'] = max_slices
        validated_data['is_valid_cake'] = CakeValidator().is_valid(validated_data)
        return ModelSerializer.create(self, validated_data)

    class Meta:
        model = models.Cake 
        exclude = ['created_timestamp', 'modified_timestamp']
        #NB: We update these in create but don't allow them in the input
        read_only_fields = ('max_slices', 'is_valid_cake',) 