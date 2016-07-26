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
        # Jun inputs her resume
        yaml_resume = """
        header:
                name : Jun McResume
                address : 30 Pleasent St.
    		city : Suburbian
    		state: Texas
    		zipcode : 12345
    		phone : '+1 (XXX)XXX-XXXX'
			email : 'cliche@aol.net'
    	
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
        # Jun runs the resume through the engine
        generator.run_yaml(yaml_resume, categories = ['Education','Work'], emphasis = ['education','industry'], year = 2014)
        
        # Jun examines the produced LaTeX file
        self.fail('finish writing the functional test')
        
        # Jun ensures the header is properly formated the latex file
        
        # Jun ensures 'Education' appears as a header in the file
        
        # Jun ensures the point on ____ does not appear in the file
        
        # Jun ensures that category points are rendered effectively
        
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
