'''
Created on May 8, 2019

@author: tom
'''

#lower case letters only

#What constitutes valid order?
#-We need to each of m minions a slice of cake with the same sequence of candies 
#-It appears as if the problem statement allow us ot toss out extras slices 
#-So the number of minions m must be <= max number of equal sequence slices
# Now here's the tricky part:  ""abcabcabcabc" is ok.  but so is "bcabcabcabca"

import re 


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
            raise Exception("The cake must have candies")
        if not CandiesFormatVaildator().is_valid(candies):
            raise Exception("The candies are not valid.")
 
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
        

            
    