"""
Instructions
Develop a set of classes for a college to use in various student service and personnel applications. 

Classes you need to design include the following:

Person - A Person contains a first name, last name, street address, zip code, and phone number. The class also includes a method that sets each data field, using a series of dialog boxes and a display method that displays all of a Person’s information on a single line at the command line on the screen.

CollegeEmployee - CollegeEmployee descends from Person. A CollegeEmployee also includes a Social Security number, an annual salary, and a department name, as well as methods that override the Person methods to accept and display all CollegeEmployee data.

Faculty - Faculty descends from CollegeEmployee. This class also includes a Boolean field that indicates whether the Faculty member is tenured, as well as methods that override the CollegeEmployee methods to accept and display this additional piece of information.

Student - Student descends from Person. In addition to the fields available in Person, a Student contains a major field of study and a grade point average as well as methods that override the Person methods to accept and display these additional facts.

Write an application named CollegeList that implements a list of four “regular” CollegeEmployee, three Faculty, and seven Students. 

1. Prompt the user to specify which type of person’s data will be entered (C, F, or S), or allow the user to quit (Q). While the user chooses to continue (that is, does not quit), accept data entry for the appropriate type of Person. 

2. If the user attempts to enter data for more than four CollegeEmployees, three Faculty, or seven Students, display an error message. 

3. When the user quits, display a report on the screen listing each group of Persons under the appropriate heading of “College Employees,” “Faculty,” or “Students.” 

4. If the user has not entered data for one or more types of Persons during a session, display an appropriate message under the appropriate heading.

Save the files as Person.py, CollegeEmployee.py, Faculty.py, Student.py, and CollegeList.py.

Program description

Programmer: Your Last Name, Your First Name

Course: CSC1019-FBN

'''

 Zip your 4 Python programs into LastNameFirstInitial_Project4.zip and submit it to the Project 4 folder under Assignments tab.
"""

