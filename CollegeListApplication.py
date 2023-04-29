"""
Program Description: Program ask user for a series of inputs for different classes and fields consisting of a person, student, college employee, and faculty.
The user will then be presented with all inputs from each class in their appropriate headings.

Programmer: Cox, Brandon

Course: CSC1019-FBN

"""
from Person import Person
from Student import Student
from CollegeEmployee import CollegeEmployee
from Faculty import Faculty


p = [] #create array this will be used for attributes within class instance
def person(): #create function for inputs
  flag = True #create flag for while loop
  while flag == True:
    for x in range(1): #use for loop and range of 1 to repeat once
      firstName = input("\nPlease Enter Your First Name: ")
      if firstName == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      lastName = input("Please Enter Your Last Name: ")
      if lastName == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      streetAddress = input("Please Enter Your Street Address: ")
      if streetAddress == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      zipCode = input("Please Enter Your Zip Code: ")
      if zipCode == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      phoneNumber = input("Please Enter Your Phone Number: ")
      if phoneNumber == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
        
      flag = False #break loop with flag

  return firstName, lastName, streetAddress, zipCode, phoneNumber #return values

s = [] # create array this will be used for attributes within class instance
def student(): #create function for inputs
  flag = True #create flag for while loop
  while flag == True:
    for x in range(1): #use for loop and range of 1 to repeat once
      study = input("What Is Your Field Of Study?: ")
      if study == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      gpa = input("Please Enter Your GPA: ")
      if gpa == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break

      flag = False #break loop with flag
        
  return study, gpa #return values

c = [] # create array this will be used for attributes within class instance
def collegeEmpoyee(): #create function for inputs
  flag = True #create flag for while loop
  while flag == True:
    for x in range(1): #use for loop and range of 1 to repeat once
      social = input("Please Enter Your Social Security Number: ")
      if social == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      salary = input("Please Enter Your Annual Salary: ")
      if salary == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
      department = input("Please Enter Your Department Name: ")
      if department == "": #error handler if nothing is entered
        print("\nYou didn't enter anything\n")
        break
        
      flag = False #break loop with flag
      
  return social, salary, department #return values

f = []  #create array this will be used for attributes within class instance
def faculty(): #create function for inputs
  flag = True #create flag for while loop
  tenuredBool = True #create tenured variable for boolean value 
  while flag == True:
    for x in range(1): #use for loop and range of 1 to repeat once
      tenured = input("Are you tenured? (Y/N): ")
      upperTenured = tenured.upper() #apply upper function for error handling on input
      if upperTenured == "N":
        tenuredBool = False #if input is no set tenured variable to false
      elif upperTenured == "Y":
        tenuredBool = True #if input is yes set tenured variable to true
      elif upperTenured != "Y" or upperTenured != "N": #error handling if input is not Y or N
        print("\nYou did not enter (Y/N)\n")
        break
    
      flag = False #break loop with flag
      
  return tenuredBool #return values
  
flag = True #create flag for while loop
cCount = 0 #create count for x amount of looping for college employee input for assignment rubric
sCount = 0 #create count for x amount of looping for student input for assignment rubric
fCount = 0 #create count for x amount of looping for faculty input for assignment rubric
while True: #create loop for user input
  if flag == False: #create if statement for bug handling
    flag = True
  if cCount == 4 and sCount == 7 and fCount == 3: #create if statement for bug handling
    break

  while True: #create nested while loop for input

    dataPrompt = input("\nWhich type of user do you want to enter? Student(S), College Employee(C), or Faculty?(F) or enter (Q) to quit: ")
    print("\n------------------------")


    upper = dataPrompt.upper() #apply uper function for error handling
  
    if upper == "Q": #if user enters Q break loop
      break
    
  
    elif upper == "S": #if user enters S continue with student input
      flag = True #create flag for while loop

      while flag == True:
        if sCount >= 7: #if statement for count to break loop if user has entered too many inputs
          print(f"\nYou have hit your max input of {sCount}\n")
          print("------------------------")
          break

        p.append(person()) #append global person array and call person function for user inputs
        s.append(student()) #append global student array and call student function for user inputs
    
        personClass = Person(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4]) #instantiate class and apply each corresponding index within the inputs for attributes
        studentClass = Student(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4], s[0][0],s[0][1])
          
        studentClass.append() #call student class method to append global array into class array
    
        p.clear() #clear global array for new inputs
        s.clear() #clear global array for new inputs
  
        sCount += 1 #add 1 to count for every iteration, if count is too high user cannot add any more inputs

        print("\n------------------------\n")


        while True: #create while loop to ask user if they want to input and user
          
          ask = input("Do you want to enter another student? (7 Max) (Y/N): ")
          upperAsk = ask.upper() #apply upper function for error handling
          
          if sCount >= 7: #if statement for count to break loop if user has entered too many inputs
            flag = False #if user has entered too many users set flag to false so loop will not continue
            print(f"\nYou have hit your max input of {sCount}\n")
            print("------------------------")
            break
          elif upperAsk == "Y": #if user enters yes break out of nested while loop and continue out looper again
            print(f"\nYour total entered students are: {sCount}")
            print("\n------------------------")
            break
          elif upperAsk == "N": #if user enters no set flag to false and break out of both loops
            print(f"\nYour total entered students are: {sCount}\n")
            print("------------------------")
            flag = False #set flag to false to break out of outer loop
            break
          elif upperAsk != "Y" or upperAsk != "N": #error handling if user does not enter Y or N
            print("\nYou did not enter (Y/N)")
            continue
            


  
      
    elif upper == "C": #if user enters C continue with college employee input
      flag = True #create flag for while loop

      while flag == True:
        if cCount >= 4: #if statement for count to break loop if user has entered too many inputs
          print(f"\nYou have hit your max input of {cCount}\n")
          print("------------------------")
          break
  
        p.append(person()) #append global person array and call person function for user inputs
        c.append(collegeEmpoyee()) #append global college employee array and call college employee function for user inputs
        
        personClass = Person(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4]) #instantiate class and apply each corresponding index within the inputs for attributes
        collegeEmployeeClass = CollegeEmployee(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4],c[0][0],c[0][1],c[0][2])
            
        collegeEmployeeClass.append() #call college employee class method to append global array into class array
      
        p.clear() #clear global array for new inputs
        c.clear() #clear global array for new inputs
  
        cCount += 1 #add 1 to count for every iteration, if count is too high user cannot add any more inputs
        
        print("\n------------------------\n")
        
        while True: #create while loop to ask user if they want to input and user
          
          ask = input("\nDo you want to enter another college employee? (4 Max) (Y/N): ")
          upperAsk = ask.upper() #apply upper function for error handling
          
          if cCount >= 4: #if statement for count to break loop if user has entered too many inputs
            flag = False #if user has entered too many users set flag to false so loop will not continue
            print(f"\nYou have hit your max input of {cCount}\n")
            print("------------------------")
            break
          elif upperAsk == "Y": #if user enters yes break out of nested while loop and continue out looper again
            print(f"\nYour total entered college employees are: {cCount}")
            print("\n------------------------")
            break
          elif upperAsk == "N": #if user enters no set flag to false and break out of both loops
            print(f"\nYour total entered college employees are: {cCount}\n")
            print("------------------------")
            flag = False #set flag to false to break out of outer loop
            break
          elif upperAsk != "Y" or upperAsk != "N": #error handling if user does not enter Y or N
            print("\nYou did not enter (Y/N)")
            continue
  
          
        
    elif upper == "F": #if user enters F continue with faculty input
      flag = True #create flag for while loop

      while flag == True:
        if fCount >= 3: #if statement for count to break loop if user has entered too many inputs
          print(f"\nYou have hit your max input of {fCount}\n")
          print("------------------------")
          break

        p.append(person()) #append global person array and call person function for user inputs
        c.append(collegeEmpoyee()) #append global college employee array and call college employee function for user inputs
        f.append(faculty()) #append global faculty array and call faculty function for user inputs
        personClass = Person(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4]) #instantiate class and apply each corresponding index within the inputs for attributes
        collegeEmployeeClass = CollegeEmployee(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4],c[0][0],c[0][1],c[0][2])
        facultyClass = Faculty(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4],c[0][0],c[0][1],c[0][2],f[0])
          
        facultyClass.append() #call faculty class method to append global array into class array
    
        p.clear() #clear global array for new inputs
        c.clear() #clear global array for new inputs
        f.clear() #clear global array for new inputs
            
        fCount += 1 #add 1 to count for every iteration, if count is too high user cannot add any more inputs
        
        print("\n------------------------\n")
        
        while True: #create while loop to ask user if they want to input and user

          ask = input("\nDo you want to enter another faculty employee? (3 Max) (Y/N): ")
          upperAsk = ask.upper() #apply upper function for error handling

          if fCount >= 3: #if statement for count to break loop if user has entered too many inputs
            flag = False #if user has entered too many users set flag to false so loop will not continue
            print(f"\nYou have hit your max input of {fCount}\n")
            print("------------------------")
            break
      
          elif upperAsk == "Y": #if user enters yes break out of nested while loop and continue out looper again
            print(f"\nYour total entered faculty are: {fCount}")
            print("\n------------------------")
            break
          elif upperAsk == "N": #if user enters no set flag to false and break out of both loops
            print(f"\nYour total entered faculty are: {fCount}\n")
            print("------------------------")
            flag = False #set flag to false to break out of outer loop
            break
          elif upperAsk != "Y" or upperAsk != "N": #error handling if user does not enter Y or N
            print("\nYou did not enter (Y/N)")
            continue


    elif upper != "Q" or upper != "S" or upper != "C" or upper != "F": #create error handling if user doesn't enter Q, S, C, or F
      print("\nYou did not enter (S) (C) or (F)\n")
      print("------------------------")
  break #break out of loop
  
Student.display() #call classmethod display to display all inputs
CollegeEmployee.display() #call classmethod display to display all inputs
Faculty.display() #call classmethod display to display all inputs