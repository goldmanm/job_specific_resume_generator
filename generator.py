# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:18:18 2016

@author: mark
"""

from backend import *
from api import *
#from os import 
import yaml

def prepare_resume_data():
    try:
        import resume_data
    
    except:
        datafile = input('What datafile stores your resume?')
        from shutil import copyfile
        copyfile(datafile,'resume_data.py')
    
    
def prepare_resume_preferences():
    try:
        import resume_preferences
    
    except:
        datafile = input('What datafile stores your build_preferences?')
        from shutil import copyfile
        copyfile(datafile,'resume_preferences.py')
    
    
if __name__ =='__main__':
    prepare_resume_data()
    prepare_resume_preferences()
    import resume_preferences as pref
    import resume_data as data
    pref = DocumentPreferences(data.desired_categories,data.desired_year,data.desired_emphasis)
    write(makeheader())
    write(begindocument())

    
    # makes name logo of the document
    write(header(data.name,data.address,data.city,data.state,data.zipcode,data.phone,data.email))
    
    for category in data.categories:
        if category.name in pref.categories:
            writeobj(category,pref)
            
        
    
    write(enddocument())
    
def get_raw_python_from_yaml(yaml_string):
    return yaml.load(yaml_string)
    
def process_header_from_raw_data(raw_python):
    header = raw_python['header']
    return header
    
def create_point_objects_from_point_list(raw_python):
    """
    input a list of dictionaries of point attributes
    ensure proper keys or throw error
    return list of point objects
    """
    raise NotImplementedError()
    
def create_task_objects_from_task_list(raw_python):
    """
    input a list of dictionaries of task attributes
    ensure proper keys or throw error
    return list of task objects
    """
    raise NotImplementedError()
    
def create_category_objects_from_category_lists(raw_python):
    """
    input a list of dictionaries of category attributes
    ensure proper keys or throw error
    return list of category objects
    """
    raise NotImplementedError()