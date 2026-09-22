class Employee :
    # name = "Nabeel"
    language = "Python" # This is a class attribute
    salary= 1200000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good morning")


nabeel = Employee()
# nabeel.language  ="JavaScript"# This is an instance attribute
# print( nabeel.language , nabeel.salary)
nabeel.getInfo()
nabeel.greet()
# Employee.getInfo(nabeel)

