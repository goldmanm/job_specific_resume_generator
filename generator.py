# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:18:18 2016

@author: mark
"""

import backend
import api
#from os import 
import yaml
import sys,getopt

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
        points.append(api.Point(point['text']))
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
        tasks.append(api.Task(task['name']))
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
    
def process_list_category_dicts_to_python_objects(raw_python):
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
        sections.append(api.Category(section['topic']))
        if 'year' in section.keys():
            sections[-1].year = section['year']
        if 'emphasis' in section.keys():
            sections[-1].emphasis = section['emphasis']
        if 'tasks' in section.keys():
            sections[-1].tasks = create_task_objects_from_task_list(section['tasks'])
        if 'points' in section.keys():
            sections[-1].points = create_point_objects_from_point_list(section['points'])
    return sections
    

def prepare_resume_data(resume_file):
    
    reader = open(resume_file,'r')
    resume_text = reader.read()
    resume_raw_python = yaml.load(resume_text)
    header = process_header_from_raw_data(resume_raw_python)
    list_of_category_dicts = process_body_from_raw_data(resume_raw_python)
    category_list = process_list_category_dicts_to_python_objects(list_of_category_dicts)
    reader.close()
    return header, category_list
    
def prepare_resume_preferences(preferences_file):
    if preferences_file =='':
        reader = open('default_preferences.yml','r')
    else:
        reader = open(preferences_file,'r')
    preferences_text = reader.read()
    preference_dict = yaml.load(preferences_text)
    pref = api.DocumentPreferences(preference_dict['desired categories'],
                               preference_dict['desired year'],
                                preference_dict['desired emphasis'])
    pref.all_emph(preference_dict['acceptable emphasis'])
    reader.close()
    return pref
    
def set_writing_file(file_name):
    if file_name == '':
        backend.file_writer = open('temp_tex_resume.tex','w')
    else:
        backend.file_writer = open(file_name,'w')
    #return file_writer
        
def parse_arguments(arguments):
    usage = 'generatory.py -d test.yml -p preferences.py -o output.tex'
    input_file = ''
    output_file = ''
    preferences_file = ''
    
    try:
        opts,args = getopt.getopt(arguments,"hd:p:o:",["data",'preferences','tex-output'])
    except getopt.GetoptError:
        raise getopt.GetoptError(usage)
    for option, argument in opts:
        if option == '-h':
            print(usage)
            sys.exit()
        elif option in ('-d','--data'):
            input_file = argument
        elif option in ('-o','--output'):
            output_file = argument
        elif option in ('-p','--preferences'):
            preferences_file=argument
    return input_file, preferences_file, output_file
    
if __name__ =='__main__':
    resume_file, resume_preferences, output_file_name = parse_arguments(sys.argv[1:])
    set_writing_file(output_file_name)
    hd, category_list = prepare_resume_data(resume_file)
    pref = prepare_resume_preferences(resume_preferences)
    # check that input of resume preferences match
    category_list_names = [cat.name for cat in category_list]
    for cat in pref.categories:
        if cat not in category_list_names:
            raise AttributeError('`{0}` not in list of categories'.format(cat))
    backend.write(backend.makeheader())
    backend.write(backend.begindocument())
    # makes name logo of the document
    backend.write(api.header(hd['name'], hd['address'],hd['city'],hd['state'],hd['zipcode'], hd['phone'],hd['email']))
    for category in category_list:
        if category.name in pref.categories:
            backend.writeobj(category,pref)
            
    
    
    backend.write(backend.enddocument())
    
