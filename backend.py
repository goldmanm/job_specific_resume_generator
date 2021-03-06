# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:56:14 2016

@author: mark
"""
from api import *

file_writer = None
def write(text, process_text=True):
    """
    writes text into the document in a format to be decided later
    """
    if process_text:
        text = text.replace('%','\%')
        text = text.replace('&','\&')
        text = text.replace('$','\$')
        text = text.replace('\\$','$')
    file_writer.write(text)
    
def writeobj(obj, pref):
    """
    this method outputs text for a Category, Task, or Point using recursive
    algorythem and checking to see if the document's desired_emphasis allows
    for the item to be printed.
    obj = an item of Category, Task, or Point class
    pref = desired emphasis of the document
    """
    
    if pref.judge(obj):
        if isinstance(obj,Point):
            return r"\item[] " + obj.text
        elif isinstance(obj,Task):
            string = r"\headercondensed{%s}{%s}{%s}" % (obj.title,obj.entity,obj.dates)
            if obj.points != []:
                points_string = ''
                for point in obj.points:
                    points_string += writeobj(point,pref)
                if points_string: # valid points are identified
                    string += r"\begin{itemize}"
                    string += points_string
                    string += r"""\end{itemize}
                    
                              \vspace{0.5em}"""
        elif isinstance(obj,Category):
            string = r"\subsection*{%s}" % (obj.name)
            if obj.tasks != [] or obj.points != []:
                string += r"\begin{indentsection}{\parindent} \parskip=0.0em"
                if obj.tasks != []:
                    for task in obj.tasks:
                        string += writeobj(task,pref)
                if obj.points != []:
                    points_string = ''
                    for point in obj.points:
                        points_string += writeobj(point,pref)
                    if points_string: # valid points are identified
                        string += r"\begin{itemize}"
                        string += points_string
                        string += r"\end{itemize}"
                string+=r"""\end{indentsection}
                
                         \vspace{-1em}"""
        else:
            raise Exception("the class passed to writeobj is not supported. the passed class is " + str(type(obj)))
        return string
    return ''

def output(text, tag_arg=''):
    """
    outputs the text in the specified format if the tag 
    matches the resume_tags.
    tag is either '' (always matches), a string, 
    or a list of strings of acceptable tags. 
    this method can be edited to output to specific files later
    """
    if tag_arg=='' or check_match(tag_arg):
        write(text)
        
    #checks for no mistypes
    ensure_possible_tags(tag_arg)

def ensure_possible_tags(tag_arg):
    """
    checks to make sure tag_arg is in the possible_tags category.
    throws an error if it is not.
    tag_arg - a string or list of strings
    """
    if isinstance(tag_arg, str):
        if possible_tags.count(tag_arg)==0:
            raise Exception("Tag %s is not found in possible tags" %(tag_arg))
    elif isinstance(tag_arg,list):
        for tag_name in tag_arg:
            ensure_possible_tags(tag_name)
            

def makeheader():
    """
    Returns the header information for the Latex document. Currently this just
    returns the header information. In the future this may have some arguments
    for introducing extra Latex packages    
    """
    return r"""% resume.tex
% vim:set ft=tex spell:

\documentclass[10pt,letterpaper]{article}
\usepackage[letterpaper,margin=0.75in]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mdwlist}
\usepackage{textcomp}
\usepackage{tgpagella}
\usepackage{tabularx}
\pagestyle{empty}
\setlength{\tabcolsep}{0em}
\usepackage[version=4]{mhchem}
\usepackage[backend=biber,style=authoryear, bibstyle=authoryear, sorting = ynt]{biblatex}
\addbibresource{resume.bib}
% table spacing
\usepackage{enumitem}
\setlist{topsep=0.0em,itemsep=0.2em,parsep=0.0em}

% proper links
\usepackage[svgnames]{xcolor}
\usepackage[colorlinks]{hyperref}
\hypersetup{citecolor=DeepPink4}
\hypersetup{linkcolor=DarkRed}
\hypersetup{urlcolor=DarkBlue}
\usepackage{cleveref}

% indentsection style, used for sections that aren't already in lists
% that need indentation to the level of all text in the document
\newenvironment{indentsection}[1]%
{\begin{list}{}%
	{\setlength{\leftmargin}{#1}}%
	\item[]%
}
{\end{list}}

% possibly not used, remove
\newenvironment{projectsList}[1]%
{\subsection*{#1}
\begin{itemize}
	\parskip=0.1em
}
{\end{itemize}}
% possibly not used, remove
\newcommand{\inputsec}[1]
{
\vspace{-1.5em}
\input{#1}
}

% format two pieces of text, one left aligned and one right aligned
\newcommand{\headerrow}[2]
{\begin{tabular*}{\linewidth}{l@{\extracolsep{\fill}}r}
	#1 &
	#2 \\
\end{tabular*}

}

% format three pieces of text, one left aligned, one center, and one right aligned
\newcommand{\headercondensed}[3]
{\begin{tabularx}{\linewidth}{lX<{\raggedleft}@{\hspace{2em}}p{4.5em}<{\raggedleft}}
	\textbf{#1} & #2 & \emph{#3}
\end{tabularx}

}


% format intro with project, position, company, date
\newcommand{\itemintro}[4]
{
	\headerrow
		{\textbf{#1}}
		{\textbf{#3}}
	\\
	\headerrow
		{\emph{#2}}
		{\emph{#4}}
}

% make "C++" look pretty when used in text by touching up the plus signs
\newcommand{\CPP}
{C\nolinebreak[4]\hspace{-.05em}\raisebox{.22ex}{\footnotesize\bf ++}}
"""

def begindocument():
    return r"""\begin{document}
"""

def enddocument():
    return r"""\end{document}
"""    
    
