# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:18:18 2016

@author: mark
"""

from backend import *
from api import *
#from os import 

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
    