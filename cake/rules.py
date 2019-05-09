'''
Created on May 8, 2019

@author: tom
'''

import re 

from rest_framework.serializers import ValidationError

class CandiesFormatVaildator():
    '''Checks if all the candies in the list are valid'''
    
    def __init__(self):
        pass 
    
    def is_valid(self, candies):
        '''@candies: str representation of a sequence of candies 
           @returns: boolean.
        '''
        if not candies:
            return False 
        else:
            return re.fullmatch('[a-z]+', candies) is not None 

class CakeValidator():
    
    def __init__(self):
        pass 
    
    def is_valid(self, cake):
        """ 
        Parameters: 
        cake (Cake or dictionary containing cake attributes): Cake or Cake-like dictionary
      
        Returns: 
        bool: is the cake valid
      
        """
        if isinstance(cake, dict):
            number_minions = cake['number_minions']
            max_slices = cake['max_slices']
        else:
            number_minions = cake.number_minions
            max_slices = cake.max_slices
        return number_minions <= max_slices
  
  
class EqualSequenceSlicer():
    
    def __init__(self):
        pass 
    
    def get_max_slices(self, candies):
        '''
        Parameters: 
           candies (string): Representation of a sequence of candies  

        Returns: 
            int: the maximum number of slices with equivalent sequences of candies

        '''
        
        if not candies:
            raise ValidationError("The cake must have candies")
        if not CandiesFormatVaildator().is_valid(candies):
            raise ValidationError("The candies are not valid.")
 
        #Algorithm.  For each integer, i <= len(string), check if len if that string is divisible by the i
        #If it is, divide the sequence into i equal parts and check if each part is the same.
        #NB: doesn't matter where we start checking, so start at the beginning "abcabcabcabc" is ok.  but so is "bcabcabcabca"
        num_candies = len(candies)
        #NB: number of slices of cake.  Not number of cuts!
        for num_slices in range(num_candies, 0, -1):
            if num_candies % num_slices == 0:
                sequence_length = num_candies // num_slices 
                distinct_sequences = set()
                [distinct_sequences.add(candies[i:i+sequence_length]) for i in range(0, num_candies, sequence_length)]
                #if they sequences are all the same, the set has length 1
                if len(distinct_sequences) == 1:
                    return num_slices
            else:
                pass 
        

            
    