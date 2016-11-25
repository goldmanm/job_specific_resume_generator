# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:59:52 2016

@author: mark
"""

def header(name, address,city,state,zipcode, phone,email):
    return r"""
\begin{center}
{\Large \textbf{%s}}

%s\ \ \textbullet \ \ %s, %s %s
\\
%s\ \ \textbullet
\ \ %s
\end{center}
""" % (name, address,city,state,zipcode,phone,email)


def itemhead(title,company, dates, location):
    """
    makes a header logo describing the position
    """
    pass

def point(text, category=''):
    """
    places the text into the document. 
    
    text - string to put into document
    category - string or list of strings describing the emphasis of the points.
       if any of the listed strings are desired, the object will be printed.
    """
    write(text)
def bibliography ():
    pass


class Category:
    """
    Contains main section information
    name = category name used in document and to call the Category for input 
            into resume
    year = year the category became irrelevent. doesn't appear on resume
    emphasis = string or list of strings indicating it should be included in resume
    tasks = list of Task objects held by the Category object
    points = list of Point objects held by the Category object
    """
    
    def __init__(self, name, year=10000, emphasis=''):
        self.name = name
        self.year = year
        self.emphasis = emphasis
        self.tasks = []
        self.points = []
    
    def add(self,obj):
        """
        adds the Point or Task object to their specified list
        """
        if isinstance(obj,list):
            # recursively add items in list
            for item in obj:
                self.add(item)
        elif isinstance(obj,Point):
            self.points.append(obj)
        elif isinstance(obj,Task):
            self.tasks.append(obj)
        else:
            raise Exception("The object passed to 'add' function is not of accepted class. Object of class " + str(type(obj)))

class Task:
    """
    Contains information about a job or particular activity
    title = title of job or project
    dates = string of date range to put on resume
    entity = company or location or other identifying information about activity
    year = year the category became irrelevent. doesn't appear on resume
    emphasis = string or list of strings indicating it should be included in resume
    points = list of Point objects held by the Category object
    """
    
    def __init__(self,title, dates ='',entity='',year =10000, emphasis=''):
        self.title = title
        self.dates = dates
        self.entity = entity
        self.year = year
        self.emphasis = emphasis
        self.points = []
    
    def add(self,point):
        """
        adds a point to the list of points
        """
        if isinstance(point,Point):
            self.points.append(point)
        else:
            raise Exception("The object passed to 'add' function is not of accepted class. Object of class " + str(type(point)))

class Point:
    """
    short string that contains information about an activity and when it should
    be dislpayed
    text = string to display
    year = year the category became irrelevent. doesn't appear on resume
    emphasis = string or list of strings indicating it should be included in resume
    """
    
    def __init__(self, text, year =10000, emphasis =''):
        self.text = str(text)
        self.addYear(year)
        self.addEmphasis(emphasis)

    def addYear(self,year):
        if isinstance(year,int):
            self.year = year
        else:
            raise TypeError('point year must be an integer, but it is '+ str(type(year)) +
                        '. the point text is currently "'+self.text+'"')
        
    def addEmphasis(self,emphasis):
        if isinstance(emphasis,list) or isinstance(emphasis,str):
            self.emphasis = emphasis
        else:
            raise TypeError('point emphasis must be an list or string, but it is '+ str(type(emphasis)) +
                        '. the point text is currently "'+self.text+'"')

class DocumentPreferences:
    """
    stores the document preferences and has a method to determine if an item 
    should or should not be included in the set
    """
    def __init__(self,categories, year,emph):
        self.year = year
        self.emph = emph
        self.categories = categories
        
    def all_emph(self,list_of_all_emphasis):
        self.list_of_all_emphasis = list_of_all_emphasis
    def judge(self,obj):
        """
        determines whether the object should be included in the output. returns
        boolean
        """
        if obj.year > self.year and self.match_emph(obj.emphasis):
            return True
        else:
            return False
    
    def match_emph(self, other_emph):
        """
        determines whether there is a match in emphasis
        """
        if self.emph =='' or other_emph == '':
            return True
        if isinstance(other_emph, list):
            for tag_name in other_emph:
                if tag_name in self.emph:
                    return True
        elif isinstance(other_emph, str):
            if other_emph in self.emph:
                return True
        else:
            raise Exception('arguement script_tags must be a list or string')
        return False
