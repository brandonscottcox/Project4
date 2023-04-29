from CollegeEmployee import CollegeEmployee

class Faculty(CollegeEmployee): #declare subclass and inherite college employee
  nestedFacultyArray = [] #declare two arrays, nested array will be displayed
  facultyArray = [] #first array will push data into nested array and then be cleared for new data
  
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber, social, salary, department, tenured): #add attributes
    super().__init__(firstName, lastName, streetAddress, zipCode, phoneNumber, social, salary, department) #apply super function with base attributes

    self.tenured = tenured

  def append(self): #create append method this will append all attributes to array
    self.facultyArray.extend((self.firstName, self.lastName, self.streetAddress, self.zipCode, self.phoneNumber, self.social, self.salary, self.department, self.tenured))
    self.nestedFacultyArray.append(self.facultyArray[:]) #this will make a copy of the first array and append into the nested array
    self.facultyArray.clear() #clear the first array for new data
    
  @classmethod #create class method for display
  def display(cls):
    if cls.nestedFacultyArray != []: #only display if array is not empty
      displayList = "|First|", "|Last|", "|Address|", "|Zip|", "|Phone|", "|Social|", "|Salary|", "|Department|", "|Tenured|" #display titles
      
      print("Faculty:", "\n")
      print("{: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1}".format(*displayList)) #format titles
      
      for x in cls.nestedFacultyArray: #use map function to seperate multiple inputs with new lines and add commas to seperate indexes within array
        print(", ".join(map(str, x)))
        
      print("\n------------------------\n")