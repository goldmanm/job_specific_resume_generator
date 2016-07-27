# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:28:27 2016

@author: mark
"""
import unittest
from unittest import TestCase
import yaml

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
        raw_python = yaml.load(self.yaml_resume)
        self.assertEqual(raw_python['body'][0]['topic'],'Education')
        self.assertEqual(raw_python['body'][0]['tasks'][0]['points'][0]['emphasis'],
                         ['education','research'])
        
if __name__ =='__main__':
    unittest.main()