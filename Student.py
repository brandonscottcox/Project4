from Person import Person

class Student(Person): #declare subclass and inherite person
  nestedStudentArray = [] #declare two arrays, nested array will be displayed
  studentArray = [] #first array will push data into nested array and then be cleared for new data
  
  def __init__(self, firstName, lastName, streetAddress, zipCode, phoneNumber, study, gpa): #add attributes
    super().__init__(firstName, lastName, streetAddress, zipCode, phoneNumber) #apply super function with base attributes
    
    self.study = study
    self.gpa = gpa

  def append(self): #create append method this will append all attributes to array
    self.studentArray.extend((self.firstName, self.lastName, self.streetAddress, self.zipCode, self.phoneNumber, self.study, self.gpa))
    self.nestedStudentArray.append(self.studentArray[:]) #this will make a copy of the first array and append into the nested array
    self.studentArray.clear() #clear the first array for new data

  @classmethod #create class method for display
  def display(cls):
    if cls.nestedStudentArray != []: #only display if array is not empty
      displayList = "|First|", "|Last|", "|Address|", "|Zip|", "|Phone|", "|Study|", "|GPA|" #display titles
      
      print("Students:", "\n")
      print("{: >1} {: >1} {: >1} {: >1} {: >1} {: >1} {: >1}".format(*displayList)) #format titles
      
      for x in cls.nestedStudentArray: #use map function to seperate multiple inputs with new lines and add commas to seperate indexes within array
        print(", ".join(map(str, x)))
        
      print("\n------------------------\n")