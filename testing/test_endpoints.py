'''
Created on May 8, 2019

@author: tom
'''

from django.test import TestCase 
from cake.models import Cake
from rest_framework.test import APIClient




#TODO: figure out why reverse isn't working and replace the CAKE_URL with reverse
class TestCake(TestCase):
    
    CAKE_URL = '/cake/'
    
    def setUp(self):
        self.cake1 = Cake.objects.create(display_name='Cake1',
                          candies='abcabcabc',
                          max_slices = 3,
                          number_minions = 2,
                          is_valid_cake = True)
        self.cake2 = Cake.objects.create(display_name='Cake2',
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
        response = client.post(self.CAKE_URL, data)
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
        response = client.post(self.CAKE_URL, data)
        self.assertEqual(response.status_code, 201)
        
        new_cake = Cake.objects.get(display_name = display_name)
        self.assertEqual(new_cake.candies, toppings_string)
        self.assertEqual(new_cake.max_slices, 3)
        self.assertEqual(new_cake.number_minions, 5)
        self.assertFalse(new_cake.is_valid_cake)    
          
         
    def test_create_cake_invalid_toppings(self):
        display_name ='test_create_cake_invalid_toppings'
        toppings_string = 'ab bab'
        data = {'display_name': display_name, 
                'candies': toppings_string,
                'number_minions': 5}
        client = APIClient()
        response = client.post(self.CAKE_URL, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Cake.objects.filter(display_name=display_name).count(), 0)

    def test_get_cake_via_display_name(self):
        expected_data = {'id': 1, 'display_name': 'Cake1', 
                         'candies': 'abcabcabc', 
                         'max_slices': 3, 
                         'number_minions': 2, 'is_valid_cake': True}
        client = APIClient()
        url = '{base}{display_name}/'.format(base=self.CAKE_URL, display_name=self.cake1.display_name)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)   
    
    def test_get_cake_via_display_name_not_found(self):
        client = APIClient()
        url = '{base}{display_name}/'.format(base=self.CAKE_URL, display_name='fooobarcake')
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_list_cakes(self):     
        client = APIClient()
        url = self.CAKE_URL
        response = client.get(url)
        
        expected_cake_1_data = {'id': 1, 'display_name': 'Cake1', 
                 'candies': 'abcabcabc', 
                 'max_slices': 3, 
                 'number_minions': 2, 'is_valid_cake': True}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        cake_1_data = dict(list(filter(lambda x: x['id'] == self.cake1.id, response.data))[0])
        self.assertEqual(cake_1_data, expected_cake_1_data)
        
    def test_partial_update_cakes(self):
        client = APIClient()
        expected_data = {'id': 1, 'display_name': 'Cake1', 
         'candies': 'abcabcabc', 
         'max_slices': 3, 
         'number_minions': 10, 'is_valid_cake': False}  
        #NB: we invalidated the cake because there are too many minions
        
        url = '{base}{display_name}/'.format(base=self.CAKE_URL, display_name=self.cake1.display_name)
        data = {'number_minions':10}
        response = client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)                 
        
    def test_partial_update_is_valid_not_allowed(self):
        client = APIClient()
        url = '{base}{display_name}/'.format(base=self.CAKE_URL, display_name=self.cake1.display_name)
        data = {'is_valid_cake': False}

        response = client.patch(url, data)      
        self.assertEqual(response.status_code, 400)
        self.cake1.refresh_from_db()
        self.assertTrue(self.cake1.is_valid_cake)             
        
    def test_partial_update_max_slices_not_allowed(self):
        client = APIClient()
        url = '{base}{display_name}/'.format(base=self.CAKE_URL, display_name=self.cake1.display_name)
        data = {'max_slices': 120}

        response = client.patch(url, data)      
        self.assertEqual(response.status_code, 400)
        self.cake1.refresh_from_db()
        self.assertEqual(self.cake1.max_slices, 3)      
        
    def test_full_update_not_allowed(self):  
        client = APIClient()
        url = '{base}{display_name}/'.format(base=self.CAKE_URL, display_name=self.cake1.display_name)
        data = {'number_minions': 120}

        response = client.put(url, data)      
        self.assertEqual(response.status_code, 400)
        self.cake1.refresh_from_db()
        self.assertEqual(self.cake1.number_minions, 2)                   
        
        
                
#     