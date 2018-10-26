# Python Resume Generator

Many jobs require tailored resumes. A position at an advertising agency might require different knowledge, skills and experience than one in government or engineering. After trying to keep various versions of resumes for all the things I've applied for while in school, I ended up with a  hodgepodge of various font sizes and irrelevant factoids scattered across many Word files. When I want to refine my resume, I manually copy and paste from various places, correct errors, and write new stuff, just creating another version to go through. I tried looking for better methods or programs to easily modify and manage resumes, but couldn't find one that fit my qualifications.

This program is designed to automate some of the slicing and dicing I had done previously. You create a main file with all your information, and create another file which specifies which parts of the information to emphasize. The program then converts your information to a LaTeK file which is then made into your resume.

Keeping your resume up to date will still take time, but I hope this tool allows you to modify it with ease.

## installation

These files can be used directly from the command line window on Linux systems (and possibly Mac, though it hasn't been tested). For Windows 10 systems, you can download an Ubuntu terminal from the app store to run this software.

This software requires `pdflatex` as well as python 3 with the `yaml` package. Python can be installed through various python managers and `pdflatex` can be obtained from Linux package manager systems.

## designing your resume

Your resume will consist of two files, one with your information, called 'main' here, and one containing the pieces of information you want to output, called 'preferences'. You can see examples of these file in the folder `personal_resume`. Both of these files use yaml syntax which is essentially a flexible structure containing lists and hash structures.

Let's look at the example of Surya Patel, who is making resumes for college and welding school. Here's the header of his resume, which will appear at the top of Surya's final PDF:

```yaml
header:
  name   : Surya Patel
  address: 12345 Example St.
  city   : Washington
  state  : PA
  zipcode: 01234
  phone  : '+1 (212)867-5309'
  email  : 'professional_email_name@personal_email_provider.com'
```

The rest of his resume information is under the `body:` key, which consists of a list of categories. One of Surya's important categories is his Education, shown below.

```yaml
  - topic : Education
    year  : 2019
    tasks : 
    - name: Diploma
      time: 2019
      org : Washington High School
      points:
      - text: GPA: 4.3/5
        emphasis: ['college', 'cat sitting']
      - text: \textbf{courses}: Industrial Design I, Industrial Design II, Spanish, Karate
        emphasis: welding
      - text: \textbf{courses}: Calculus, Chemistry, Advanced Physics, Spanish
        emphasis: college
      - text: Fastest car in car design competition
        emphasis: welding
    - name: Graduated
      time: 2015
      year: 2015
      org: Sacajawea Middle School
      emphasis: college
    points:
    - text: Franklin Elementary
      emphasis: college
```

There are three classes of objects created in this format. The top `Category` contains all the information about Surya's education. `Category`s can store what it is called (topic), what year it was completed (year, used for filtering), and can contain lists of `Task` and `Point` objects. 

`Task`s are kind of like the project level, where you can specify the name of the position, or in this case degree (name), where you held the position (org), a year (again for filtering), and the date associated with it, which appears on the resume (time). `Task` objects can also contain `Points`.

`Points` are the lowest level and are essentially a line of text, and they can belong to either `Category` or `Task` objects.

The last attribute which can be applied to any of these objects is `emphasis`. This is the most important part of how this resume generator is designed. When you decide to create a resume, you specify a list of emphases you want the resume to include. If an object does not have an `emphasis` attribute, it will always be included (though `Category` exclusion can also be specified in the preferences file)

Surya applies `emphasis` attribute to specify whether he wants the information to appear in his college applications or welding applications. Since his diploma from Washington High School doesn't have an emphasis parameter, it will appear on whatever resume he creates that has Education. However, Surya only wants his resume to contain his Middle School information if it is his college application.

Objects can have multiple emphasis, which would just use the list syntax of python.

```yaml
emphasis: ['college', 'cat sitting']
```
If nothing is input, the items will always appear in your resume 

Note that this program will automatically convert `%`, `&`, `$` from the yaml file to escaped code which properly works in latex: %, &, $, ... If you want to use inline equations with latex, please put `\$` instead of `$`. The engine will convert it to properly display the equation.

## making a preferences file

When you want to apply to a role with different requirements, you should change your preferences file. A preference file has four attributes: 

* `acceptable emphasis`: this lists all the types of emphasis in your complete resume and is used for checking for warning about misspellings.
* `desired emphasis`: list describing which emphasis you want in this resume.
* `desired categories`: list describing the order of the major sections you want included.
* `desired year`: will only include things after this year, so you don't have to remove old information.

You can see an example in the `personal_resume` folder.

## running your resume

Currently there is a two step process to make your resume. This may be made into one when an interface between `pdflatex` and `python` is made reliably.

**prerequisites**: resume yaml file, preferences yaml file

**step 1**: `python generator.py -d <path-to-resume>.yml -p <path-to-preferences>.yml -o <path-to-output-file>.tex`

**step 2**: `pdflatex -synctex=1 -interaction=nonstopmode <path-to-tex-file>.tex`or open up your favorite Tex-editor

This process is simplified in the `personal_resume` folder using a Makefile. Just type `make tex` followed by `make pdf`.


