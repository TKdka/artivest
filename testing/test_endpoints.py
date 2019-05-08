'''
Created on May 8, 2019

@author: tom
'''

from django.test import TestCase 
from cake.models import Cake
from rest_framework.test import APIClient

class TestCake(TestCase):
    
    CREATE_URL = '/cake/'
    
    def setUp(self):
        self.cake1 = Cake(display_name='Cake1',
                          candies='abcabcabc',
                          max_slices = 3,
                          number_minions = 2,
                          is_valid_cake = True)
        self.cake2 = Cake(display_name='Cake1',
                      candies='xyxyxyxy',
                      max_slices = 4,
                      number_minions = 5,
                      is_valid_cake = False)
    
    
    
    def test_crete_cake(self):
        display_name ='test_create_cake'
        toppings_string = 'ababab'
        data = {'display_name': display_name, 
                'candies': toppings_string,
                'number_minions': 2}
        client = APIClient()
        response = client.post(self.CREATE_URL, data)
        self.assertEqual(response.status_code, 201)
        
        new_cake = Cake.objects.get(display_name = display_name)
        self.assertEqual(new_cake.candies, toppings_string)
        self.assertEqual(new_cake.max_slices, 3)
        self.assertEqual(new_cake.number_minions, 2)
        self.assertTrue(new_cake.is_valid_cake)
    
    def test_create_cake_not_valid_cake(self):
        display_name ='test_create_cake_not_valid_cake'
        toppings_string = 'ababab'
        data = {'display_name': display_name, 
                'candies': toppings_string,
                'number_minions': 5}
        client = APIClient()
        response = client.post(self.CREATE_URL, data)
        self.assertEqual(response.status_code, 201)
        
        new_cake = Cake.objects.get(display_name = display_name)
        self.assertEqual(new_cake.candies, toppings_string)
        self.assertEqual(new_cake.max_slices, 3)
        self.assertEqual(new_cake.number_minions, 5)
        self.assertFalse(new_cake.is_valid_cake)    
          
         
#     def test_crete_cake_invalid_toppings(self):
#         
#     