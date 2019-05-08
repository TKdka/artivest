'''
Created on May 8, 2019

@author: tom
'''

from django import test 

from cake.rules import EqualSequenceSlicer, CandiesFormatVaildator

class EqualSequenceSlicerEqualSequenceSlices(test.TestCase):
    
    def test_none(self):
        self.assertRaises(Exception, EqualSequenceSlicer().get_max_slices, (None) )
        
    def test_empty(self):
        self.assertRaises(Exception, EqualSequenceSlicer().get_max_slices, ([]) )
        
    def test_all_different(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('abcdefg'),1)
        
    def test_two_slices(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('abcabc'),2)
        
    def test_three_slices(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('ababab'),3)
        
    def test_all_same(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('aaaaa'),5)

    def test_single_extra_candy_in_middle(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('abczabcabc'),1)                                
        
    def test_single_extra_candy_at_start(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('zabcabcabc'),1)                                
        
    def test_single_extra_candy_at_end(self):
        self.assertEqual(EqualSequenceSlicer().get_max_slices('abcabcabcz'),1)                     
        
class TestCandiesFormatVaildator(test.TestCase):
    
    def test_none(self):
        self.assertFalse(CandiesFormatVaildator().is_valid(None))           
        
    def test_empty(self):
        self.assertFalse(CandiesFormatVaildator().is_valid(''))           
        
    def test_single_letter(self):
        self.assertTrue(CandiesFormatVaildator().is_valid('a'))           
        
    def test_repeated_letter(self):
        self.assertTrue(CandiesFormatVaildator().is_valid('aaaaa'))           
   
    def test_standard_sequence(self):
        self.assertTrue(CandiesFormatVaildator().is_valid('ababababab'))    
        
    def test_capital_letter(self):
        self.assertFalse(CandiesFormatVaildator().is_valid('Aababababab'))    
        
    def test_number(self):
        self.assertFalse(CandiesFormatVaildator().is_valid('1ababababab'))                  
 
    def test_space(self):
        self.assertFalse(CandiesFormatVaildator().is_valid('a babababab'))  
                        