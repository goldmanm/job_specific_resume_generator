# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:35:38 2016

@author: mark

This file contains a standard list of items needed to process the code.
"""
from api import *

name = 'Mark J Goldman'
address = '3314 Larkwood Lane'
city = 'Sugar Land'
state = 'TX'
zipcode = '77479'
phone = '+1 (832)971-6031'
email = 'markgoldman@mit.edu'

# write acceptable emphasis here
acceptable_emphasis = ['education','research','industry','regulatory','coding',
                         'international']

# write desired emphasis and sections here
#desired_emphasis = ['education','international']
desired_emphasis = ''
desired_categories = ['Education','Work Experience']
desired_year = 2010
# now input the resume information you'd like to store

education = Category('Education', 2019)

phd = Task('Ph.D. Chemical Engineering', '2014-2019','Massachusetts Institute of Technology')
phd.add(Point('advanced knowledge of low-termperature combustion and atmospheric aerosol formation',emphasis = ['education','research']))

mscep = Task('Masters in Chemical Engineering Practice','2016','Massachusetts Institute of Technology', 2016, emphasis = ['education','industry'])

bs = Task('Bachelors of Chemical Engineering','2014','University of Texas at Austin',2014)
bs.add(Point('GPA 4.0/4.0',emphasis = ['education']))

education.add([phd,mscep,bs])


work = Category('Work Experience')

fda = Task('Center for Drug Evaluation and Research','2016','US Food and Drug Administration',2016, emphasis=['industry','regulatory'])
fda.add(Point('designed and tested oxygen transfer capabilities of mammilian bioreactors',emphasis = 'industry'))
fda.add(Point('built contiuous crystalization system and wrote standard operating procedures',emphasis='regulatory'))

ega = Task('Proces Consultants', '2015', 'Emirates Global Aluminium, UAE',2015,emphasis=['industry','international'])



work.add([fda,ega])


# combine all the categories into one list
categories = [education,work]