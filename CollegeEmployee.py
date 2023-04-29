from Person import Person

class CollegeEmployee(Person): #declare subclass and inherite college employee
  nestedCollegeEmployeeArray = [] #declare two arrays, nested array will be displayed
  collegeEmployeeArray = [] #first array will push data into nested array and then be cleared for new data
  
  
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber, social, salary, department): #add attributes
    super().__init__(firstName, lastName, streetAddress, zipCode, phoneNumber) #apply super function with base attributes

    
    self.social = social
    self.salary = salary
    self.department = department

  def append(self): #create append method this will append all attributes to array
    self.collegeEmployeeArray.extend((self.firstName, self.lastName, self.streetAddress, self.zipCode, self.phoneNumber, self.social, self.salary, self.department))
    self.nestedCollegeEmployeeArray.append(self.collegeEmployeeArray[:]) #this will make a copy of the first array and append into the nested array
    self.collegeEmployeeArray.clear() #clear the first array for new data




  @classmethod #create class method for display
  def display(cls):
    if cls.nestedCollegeEmployeeArray != []: #only display if array is not empty
      displayList = "|First|", "|Last|", "|Address|", "|Zip|", "|Phone|", "|Social|", "|Salary|", "|Department|" #display titles
      
      print("College Employees:", "\n")
      print("{: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1}".format(*displayList))#format titles

      for x in cls.nestedCollegeEmployeeArray:#use map function to seperate multiple inputs with new lines and add commas to seperate indexes within array
        print(", ".join(map(str, x)))

      print("\n------------------------\n")