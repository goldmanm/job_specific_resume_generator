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
import backend
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
        
#    def test_if_body_list_converted_to_objects(self):
#        raw_python = generator.get_raw_python_from_yaml(self.yaml_resume)
#        body_raw = generator.process_body_from_raw_data(raw_python)
#        self.categories = generator.process_body_to_python_objects(body_raw)
#        self.fail('figure out what this test does')
        
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
        task_list_yaml="""
    - name : Ph.D. Engineering
      time : 2010-2012
      org  : Massachusetts Institute of Technology
      points:
      - text: advanced knowledge of catalytic systems for biogas recovery
        emphasis: ['education','research']
    - name : B.S. Engineering
      time : 2008-2010
      org  : University of Moscow
      year : 2015
      emphasis : ['undergraduate']
      points:
      - text : solved world hunger
      - text : ate 3 packs of potato chips
        emphasis: ['diet']
        
        """
        raw_python = yaml.load(task_list_yaml)
        tasks = generator.create_task_objects_from_task_list(raw_python)
        self.assertEqual(len(tasks), 2)
        self.assertIsInstance(tasks[0],api.Task)
        self.assertEqual(tasks[1].dates,'2008-2010')
        self.assertIsInstance(tasks[0].points[0].emphasis[0],str)
        self.assertEqual(tasks[1].points[1].text,'ate 3 packs of potato chips')
        
        
        
    def test_if_body_objects_formed_properly(self):
        
        raw_python = generator.get_raw_python_from_yaml(self.yaml_resume)
        body_raw = generator.process_body_from_raw_data(raw_python)
        body_processed = generator.process_list_category_dicts_to_python_objects(body_raw)
        self.assertEqual(body_processed[0].tasks[0].title, 'Ph.D. Engineering')
        self.assertEqual(body_processed[0].tasks[0].points[0].text, 'advanced knowledge of catalytic systems for biogas recovery')
        self.assertEqual(body_processed[0].points[0].text, 'I got a good education')
        self.assertEqual(body_processed[1].name, 'Work')
        
    def test_output_of_prepare_resume_preferences_is_correct(self):
        
        preferences_yaml = """
        
        acceptable emphasis :
          -education
          -research
          -industry
          -regulatory
          -coding
          -international
        desired emphasis : 
          -education
        desired categories : 
          -Education
          -Work Experience
        desired year : 2010
        """
        pref = generator.prepare_resume_preferences('default_preferences.yml')
        self.assertIsInstance(pref,api.DocumentPreferences)
        
    def test_output_of_prepare_resume_data_is_correct(self):
        header, category_list = generator.prepare_resume_data('example.yml')
        self.assertIsInstance(header,dict)
        self.assertIsInstance(category_list,list)
        self.assertIsInstance(category_list[0],api.Category)

class FunctionalTests(TestCase):
    
    def setUp(self):
        
        pass
        
    def tearDown(self):
        pass
    
    def test_resume_can_be_input_as_yml_and_output_as_tex(self):
        
        # user inputs arguments into the command line 
        arguments = ['-d','example.yml',
                     '--preferences','resume_preferences.py',
                     '-o','tex/test-resume.tex']
        resume_file, resume_preferences, output_file_name = generator.parse_arguments(arguments)
        generator.set_writing_file(output_file_name)
        hd, category_list = generator.prepare_resume_data(resume_file)
        pref = generator.prepare_resume_preferences(resume_preferences)
        backend.write(backend.makeheader())
        backend.write(backend.begindocument())
        # makes name logo of the document
        backend.write(api.header(hd['name'], hd['address'],hd['city'],hd['state'],hd['zipcode'], hd['phone'],hd['email']))
        for category in category_list:
            if category.name in pref.categories:
                backend.writeobj(category,pref)
                
        
    
        backend.write(backend.enddocument())

if __name__ =='__main__':
    unittest.main()