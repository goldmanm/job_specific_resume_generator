# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:28:27 2016

@author: mark
"""
import unittest
from unittest import TestCase
import yaml
import generator
import api

class Tests(TestCase):
    
    def setUp(self):
        self.yaml_resume = """
        header:
            name : Jun McResume
            address : 30 Pleasent St.
            city : Suburbian
            state: Texas
            zipcode : 12345
            phone : '+1 (XXX)XXX-XXXX'
            email : 'cliche@aol.net'
        body:
        - topic : Education
          year  : 2017
          tasks : 
          - name : Ph.D. Engineering
            time : 2010-2012
            org  : Massachusetts Institute of Technology
            points:
            - text: advanced knowledge of catalytic systems for biogas recovery
              emphasis: ['education','research']
          points : 
          - text: I got a good education
            emphasis : ['education']
            
        - topic : Work
        """
        
    def tearDown(self):
        pass
        
        
    def test_if_yaml_to_python_is_output_properly(self):
        raw_python = generator.get_raw_python_from_yaml(self.yaml_resume)
        self.assertEqual(raw_python['body'][0]['topic'],'Education')
        self.assertEqual(raw_python['body'][0]['tasks'][0]['points'][0]['emphasis'],
                         ['education','research'])
        
    def test_if_header_dict_output_properly(self):
        raw_python = generator.get_raw_python_from_yaml(self.yaml_resume)
        header = generator.process_header_from_raw_data(raw_python)
        for item in ['name','address','city','state','zipcode','phone','email']:
            self.assertIn(item,header)
        self.assertIsInstance(header['zipcode'],str)
        
    def test_if_body_list_converted_to_objects(self):
        self.body_raw = generator.process_body_from_raw_data(self.raw_python)
        self.categories = generator.process_body_to_python_objects(self.body_raw)
        
        
    def test_if_points_formed_properly(self):
        raw_resume = """
        - text: I did a task here
          year: 2000
          emphasis: tasking
        - text: I changed the world in this internship
          year: 1974
          emphasis: ['tikunolam']
        
        """
        raw_python = yaml.load(raw_resume)
        points = generator.create_point_objects_from_point_list(raw_python)
        self.assertEqual(len(points), 2)
        self.assertIsInstance(points[0],api.Point)
        self.assertEqual(points[1].year,1974)
        self.assertEqual(points[0].text,'I did a task here')
        self.assertIsInstance(points[1].emphasis,list)
        
    def test_if_tasks_formed_properly(self):
        self.fail('finish task method')
        
        
    def test_if_body_objects_formed_properly(self):
        self.body_processed = generator.process_body_to_python_objects(self.body_raw)
        self.fail('finish writing')
        
        
        
if __name__ =='__main__':
    unittest.main()