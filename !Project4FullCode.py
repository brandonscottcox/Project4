class Person:
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.streetAddress = streetAddress
    self.zipCode =  zipCode
    self.phoneNumber = phoneNumber


class Student(Person):
  nestedStudentArray = []
  studentArray = []
  
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber, study, gpa):
    super().__init__(firstName, lastName, streetAddress, zipCode, phoneNumber)
    
    self.study = study
    self.gpa = gpa

  def append(self):
    self.studentArray.extend((self.firstName, self.lastName, self.streetAddress, self.zipCode, self.phoneNumber, self.study, self.gpa))
    self.nestedStudentArray.append(self.studentArray[:])
    self.studentArray.clear()

  @classmethod
  def display(cls):
    if cls.nestedStudentArray != []:
      displayList = "|First|", "|Last|", "|Address|", "|Zip|", "|Phone|", "|Study|", "|GPA|"
      
      print("Students:", "\n")
      print("{: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1}".format(*displayList))
      
      for x in cls.nestedStudentArray:

        print(", ".join(map(str, x)))
        
      print("\n------------------------\n")


class CollegeEmployee(Person):
  nestedCollegeEmployeeArray = []
  collegeEmployeeArray = []
  
  
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber, social, salary, department):
    super().__init__(firstName, lastName, streetAddress, zipCode, phoneNumber)

    
    self.social = social
    self.salary = salary
    self.department = department

  def append(self):
    self.collegeEmployeeArray.extend((self.firstName, self.lastName, self.streetAddress, self.zipCode, self.phoneNumber, self.social, self.salary, self.department))
    self.nestedCollegeEmployeeArray.append(self.collegeEmployeeArray[:])
    self.collegeEmployeeArray.clear()

  @classmethod
  def display(cls):
    if cls.nestedCollegeEmployeeArray != []:
      displayList = "|First|", "|Last|", "|Address|", "|Zip|", "|Phone|", "|Social|", "|Salary|", "|Department|"
      
      print("College Employees:", "\n")
      print("{: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1}".format(*displayList))
      for x in cls.nestedCollegeEmployeeArray:
        print(", ".join(map(str, x)))

      print("\n------------------------\n")


class Faculty(CollegeEmployee):
  nestedFacultyArray = []
  facultyArray = []
  
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber, social, salary, department, tenured):
    super().__init__(firstName, lastName, streetAddress, zipCode, phoneNumber, social, salary, department)

    self.tenured = tenured

  def append(self):
    self.facultyArray.extend((self.firstName, self.lastName, self.streetAddress, self.zipCode, self.phoneNumber, self.social, self.salary, self.department, self.tenured))
    self.nestedFacultyArray.append(self.facultyArray[:])
    self.facultyArray.clear()
    
  @classmethod
  def display(cls):
    if cls.nestedFacultyArray != []:
      displayList = "|First|", "|Last|", "|Address|", "|Zip|", "|Phone|", "|Social|", "|Salary|", "|Department|", "|Tenured|"
      
      print("Faculty:", "\n")
      print("{: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1}".format(*displayList))
      
      for x in cls.nestedFacultyArray: 

        print(", ".join(map(str, x)))
        
      print("\n------------------------\n")



    
p = []
def person():
  flag = True
  while flag == True:
    for x in range(1):
      firstName = input("\nPlease Enter Your First Name: ")
      if firstName == "":
        print("\nYou didn't enter anything\n")
        break
      lastName = input("Please Enter Your Last Name: ")
      if lastName == "":
        print("\nYou didn't enter anything\n")
        break
      streetAddress = input("Please Enter Your Street Address: ")
      if streetAddress == "":
        print("\nYou didn't enter anything\n")
        break
      zipCode = input("Please Enter Your Zip Code: ")
      if zipCode == "":
        print("\nYou didn't enter anything\n")
        break
      phoneNumber = input("Please Enter Your Phone Number: ")
      if phoneNumber == "":
        print("\nYou didn't enter anything\n")
        break
        
      flag = False

  return firstName, lastName, streetAddress, zipCode, phoneNumber

s = []
def student():
  flag = True
  while flag == True:
    for x in range(1):
      
      study = input("What Is Your Field Of Study?: ")
      if study == "":
        print("\nYou didn't enter anything\n")
        break
      gpa = input("Please Enter Your GPA: ")
      if gpa == "":
        print("\nYou didn't enter anything\n")
        break

      flag = False
        
  return study, gpa 

c = []
def collegeEmpoyee():
  flag = True
  while flag == True:
    for x in range(1):
      social = input("Please Enter Your Social Security Number: ")
      if social == "":
        print("\nYou didn't enter anything\n")
        break
      salary = input("Please Enter Your Annual Salary: ")
      if salary == "":
        print("\nYou didn't enter anything\n")
        break
      department = input("Please Enter Your Department Name: ")
      if department == "":
        print("\nYou didn't enter anything\n")
        break
        
      flag = False
      
  return social, salary, department

f = [] 
def faculty():
  flag = True
  tenuredBool = True
  while flag == True:
    for x in range(1):
      tenured = input("Are you tenured? (Y/N): ")
      upperTenured = tenured.upper()
      if upperTenured == "N":
        tenuredBool = False
      elif upperTenured == "Y":
        tenuredBool = True
      elif upperTenured != "Y" or upperTenured != "N":
        print("\nYou did not enter (Y/N)\n")
        break
    
      flag = False
      
  return tenuredBool
  
flag = True
cCount = 0
sCount = 0
fCount = 0
while True:
  if flag == False:
    flag = True
  if cCount == 4 and sCount == 7 and fCount == 3:
    break

  while True:

    dataPrompt = input("\nWhich type of user do you want to enter? Student(S), College Employee(C), or Faculty?(F) or enter (Q) to quit: ")
    print("\n------------------------")


    upper = dataPrompt.upper()
  
    if upper == "Q":
      break
    
  
    elif upper == "S":
      flag = True
      while flag == True:
        if sCount >= 7:
          print(f"\nYou have hit your max input of {sCount}\n")
          print("------------------------")
          break

        p.append(person())
        s.append(student())
    
        personClass = Person(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4])
        studentClass = Student(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4], s[0][0],s[0][1])


          
        studentClass.append()
    
        p.clear()
        s.clear()
  
        sCount += 1
        print("\n------------------------\n")


        while True:
          
          ask = input("Do you want to enter another student? (7 Max) (Y/N): ")
          upperAsk = ask.upper()
          
          if sCount >= 7:
            flag = False
            print(f"\nYou have hit your max input of {sCount}\n")
            print("------------------------")
            break
          elif upperAsk == "Y":
            print(f"\nYour total entered students are: {sCount}")
            print("\n------------------------")

            break
          elif upperAsk == "N":
            print(f"\nYour total entered students are: {sCount}\n")
            print("------------------------")
            flag = False
            break
          elif upperAsk != "Y" or upperAsk != "N":


            print("\nYou did not enter (Y/N)")


            continue
            


  
      
    elif upper == "C":
      flag = True
      while flag == True:
        if cCount >= 4:
          print(f"\nYou have hit your max input of {cCount}\n")
          print("------------------------")
          break
  
        p.append(person())
        c.append(collegeEmpoyee())
        
        personClass = Person(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4])
        collegeEmployeeClass = CollegeEmployee(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4],c[0][0],c[0][1],c[0][2])
            
        collegeEmployeeClass.append()
      
        p.clear()
        c.clear()
  
        cCount += 1
        
        print("\n------------------------\n")
        
        while True:
          
          ask = input("\nDo you want to enter another college employee? (4 Max) (Y/N): ")
          upperAsk = ask.upper()
          
          if cCount >= 4:
            flag = False
            print(f"\nYou have hit your max input of {cCount}\n")
            print("------------------------")
            break
          elif upperAsk == "Y":
            print(f"\nYour total entered college employees are: {cCount}")
            print("\n------------------------")
            break
          elif upperAsk == "N":
            print(f"\nYour total entered college employees are: {cCount}\n")
            print("------------------------")
            flag = False
            break
          elif upperAsk != "Y" or upperAsk != "N":
            print("\nYou did not enter (Y/N)")
            continue
  
          
        
    elif upper == "F":
      flag = True

      while flag == True:
        if fCount >= 3:
          print(f"\nYou have hit your max input of {fCount}\n")
          print("------------------------")
          break

        p.append(person())
        c.append(collegeEmpoyee())
        f.append(faculty())
        personClass = Person(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4])
        collegeEmployeeClass = CollegeEmployee(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4],c[0][0],c[0][1],c[0][2])
        facultyClass = Faculty(p[0][0], p[0][1], p[0][2], p[0][3], p[0][4],c[0][0],c[0][1],c[0][2],f[0])
          
        facultyClass.append()
  
    
        p.clear()
        c.clear()
        f.clear()
            
        fCount += 1
        
        print("\n------------------------\n")
        
        while True:
          
          ask = input("\nDo you want to enter another faculty employee? (3 Max) (Y/N): ")
          upperAsk = ask.upper()
          if fCount >= 3:
            flag = False
            print(f"\nYou have hit your max input of {fCount}\n")
            print("------------------------")
            break
      
          elif upperAsk == "Y":
            print(f"\nYour total entered faculty are: {fCount}")
            print("\n------------------------")
            break
          elif upperAsk == "N":
            print(f"\nYour total entered faculty are: {fCount}\n")
            print("------------------------")
            flag = False
            break
          elif upperAsk != "Y" or upperAsk != "N":
            print("\nYou did not enter (Y/N)")
            continue



    elif upper != "Q" or upper != "S" or upper != "C" or upper != "F":
      print("\nYou did not enter (S) (C) or (F)\n")
      print("------------------------")
  break
  
Student.display()
CollegeEmployee.display()
Faculty.display()