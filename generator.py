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
    """ 
    input whole raw yaml data and returns a dictionary of the 
    information for the header
    """
    header = raw_python['header']
    header['zipcode']=str(header['zipcode'])
    return header
    
def process_body_from_raw_data(raw_python):
    """ 
    input whole raw yaml data and returns a dictionary of the 
    information for the header
    """
    body = raw_python['body']
    return body
    
def create_point_objects_from_point_list(raw_python):
    """
    input a list of dictionaries of point attributes
    ensure proper keys or throw error
    return list of point objects
    """
    if not isinstance(raw_python, list):
        raise TypeError('input to create_point_objects_from_point_list needs to be a list. currently is ' + str(type(raw_python)))
    points = []
    for point in raw_python:
        if not isinstance(point, dict):
            raise TypeError('input to create_point_objects_from_point_list needs to be a list of dictionaries. currently is  a list of ' + str(type(point)))
        if 'text' not in point.keys():
            raise Exception('point objects must have a "text" attribute. current point contains ' + str(point))
        points.append(Point(point['text']))
        if 'year' in point.keys():
            points[-1].addYear(point['year'])
        if 'emphasis' in point.keys():
            points[-1].addEmphasis(point['emphasis'])
    return points
    
def create_task_objects_from_task_list(raw_python):
    """
    input a list of dictionaries of task attributes
    ensure proper keys or throw error
    return list of task objects
    """
    
    if not isinstance(raw_python, list):
        raise TypeError('input to create_task_objects_from_task_list needs to be a list. currently is ' + str(type(raw_python)))
    tasks=[]
    for task in raw_python:
        if not isinstance(task, dict):
            raise TypeError('input to create_point_objects_from_point_list needs to be a list of dictionaries. currently is  a list of ' + str(type(task)))
        if 'name' not in task.keys():
            raise Exception('task objects must have a "name" attribute. current task contains ' + str(task))
        tasks.append(Task(task['name']))
        #add items to tasks
        if 'year' in task.keys():
            tasks[-1].year = task['year']
        if 'emphasis' in task.keys():
            tasks[-1].emphasis = task['emphasis']
        if 'time' in task.keys():
            tasks[-1].dates = task['time']
        if 'org' in task.keys():
            tasks[-1].entity = task['org']
        if 'points' in task.keys():
            tasks[-1].points = create_point_objects_from_point_list(task['points'])
    return tasks
    
def process_body_to_python_objects(raw_python):
    """
    input a list of dictionaries of sections.
    ensure proper keys or throw error
    return list of category objects
    """
    if not isinstance(raw_python, list):
        raise TypeError('input to process_body_to_python_objects needs to be a list. currently is ' + str(type(raw_python)))
    sections = []
    for section in raw_python:
        if not isinstance(section, dict):
            raise TypeError('input to create_section_objects_from_section_list needs to be a list of dictionaries. currently is  a list of ' + str(type(section)))
        if 'topic' not in section.keys():
            raise Exception('section objects must have a "topic" attribute. current section contains ' + str(section))
        sections.append(Category(section['topic']))
        if 'year' in section.keys():
            sections[-1].year = section['year']
        if 'emphasis' in section.keys():
            sections[-1].emphasis = section['emphasis']
        if 'tasks' in section.keys():
            sections[-1].tasks = create_task_objects_from_task_list(section['tasks'])
        if 'points' in section.keys():
            sections[-1].points = create_point_objects_from_point_list(section['points'])
    return sections
    
    raise NotImplementedError()