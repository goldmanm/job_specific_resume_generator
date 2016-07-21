# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest
import generator


class functional_test(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def takeDown(self):
        pass
    
    def test_input_of_resume_data(self):
        generator.prepare_resume_data()
        import resume_data as data
        
    def test_input_of_selection_criteria(self):
         generator.prepare_resume_preferences()
         import resume_preferences as pref
    
    def test_convert_yaml_to_python_objects(self):
        pass
        
        
    def converts_python_objects_to_latex(self):
        pass
        
    def converts_latex_to_pdf(self):
        pass
    
    def iterates_to_get_one_page_resume(self):
        pass
    
    def reads_page_number_of_pdf(self):
        pass        
        
        
if __name__ == '__main__':
    unittest.main()
