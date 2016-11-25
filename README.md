# Python Resume Generator

Many jobs require tailored resumes. A position at an advertising agency might focus on different aspects than that at an environmental one. Many people use 'master' resumes with all their information to subtract irrelevant information and obtain the perfect resume. I have used MS Word to keep my 'master' copy, and it is now a hodgepodge of various font sizes, information, going all the way back to highschool. When I want to refine my resume, I manually remove lots of things, write new stuff (which rarely makes it back into the 'master' copy), further complicating the resume mess.

This program is an experiment designed to as a smart master resume which can automate some of the slicing and dicing. Keeping this up to date will still take time, but I hope to make it as user friendly as possible. With that being said, it will use LaTeX to build the document, but the user will not need to know LaTeX for basic usage. 

## to do

* figure out how the frontend file should be designed
	* determine classes to write in API
* add information to my latex resume
* have a compressed list option
* have log and debug option?
* close the writing file when finished writing. 
* delete temperary file in test case & other unnecessary file
* reorganize the files (yaml conversion, tex printing, main_method separate from generating files)
* Make display of category -> points different than category -> tasks -> points
* write test to see if the emphasis is actually eliminating items from 
* throw error when misspelled section arises
* add makefile
* create spacing in printed out tex file 

* allow using a '!' as a not sign in emphasis categories. 
* throw error when topics mistyped from preferences
## installation

These files can be used directly from the command line window on linux systems (and possibly Mac, though it hasn't been tested). For windows 10 systems, you can utilize the vertual linux terminal in the Microsoft store to run this software. 

This software require `pdflatex` as well as python 3 with the `yaml` package. Python can be installed through various python managers and `pdflatex` can be obtained from linux package manager systems

## designing your resume

for those not familiar with latex, avoid using the following characters in your resume. They are escape characters in LaTeX and will throw errors. If you need to use them, replace them with the following (shown on right)

avoid these characters | replace with
--------------|-------------

When buildint the resume, you will imput information in python syntax. There are three classes of objects you will create. `Category` is used for main sections like Education, Work or Publications. It stores two other objects, `Task` and `Point`. `Task` would be something like a specific job that you can include extra information using `Point`s. `Point` objects contain a line of text to put in the resume. 

All of these objects can contain a year and a list of emphasis. When creating your resume, you can limit items based on these categories. If nothing is input, the items will always appear in your resume (though `Category`s can also be specified in the ceate file). 

## running your resume

Currently there is a two step process to make your resume. This may be made into one when an interface between `pdflatex` and `python` is made reliably.

**prerequisites**: resume yaml file, preferences yaml file

**step 1**: `python generator.py -d <path-to-resume>.yml -p <path-to-preferences>.yml -o <path-to-output-file>.tex`

**step 2**: `pdflatex -synctex=1 -interaction=nonstopmode <path-to-tex-file>.tex`or open up your favorite tex-editor

## features in the works

* a one page latex option
* a text file option
* option to imput your data as markdown or yaml
* importing data as bibtex

## project organization

section | usage
--------|---------------------------
wrapper | runs latex and checks number of pages
backend | orchistrates organization, writes latex file
API		| constains methods used by user to write their resume
frontend| this is the python file containing the user-input resume data
script	| this is where the user specifies what type of resume to create

### wrapper

The wrapper contains the protocols to call LaTeX properly in the file. I need to still figure this out. The book 'programming python' contains information about that.

### backend

The backend performs methods that write the latex file. None of these need to be called by the user in writting of their latex file. 

Methods are:

method		|		description
------------|--------------------------
write		| writes to document
output		| writes to document if tags are matched and valid
check_match | returns a boolean if the tag matches the item
ensure_possible_tags | double checks for spelling errors and throws error

This could also contain the unittests for to ensure functionality. 

### API

The API are methods that the user can utilize to write their resume for the front-end section. These are container classes with methods that convert the text into the LaTeX formatting.

### frontend



### script



### page limitations

One algorythem allows for page limitations. To achieve this, the program must be able to create the latex source, create the pdf, and analyze the pdf page length. Then adjustements can be made to the input file until the document is of the correct length.

I am not sure the optimal method to get to the correct information excluded. Some methods applicable. 

* adjust font size
* adjust spacings
* remove items described by some 'emphasis'.

It would be sad to not produce a full page when requested, which may require some second-order adjustements. 
