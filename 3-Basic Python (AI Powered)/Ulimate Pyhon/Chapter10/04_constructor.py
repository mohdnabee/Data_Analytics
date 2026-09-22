class Employee :
    # name = "Nabeel"
    language = "Python" # This is a class attribute
    salary= 1200000

    def __init__(self, name, salary, language):# dundar method which is automatically called 
      self.name = name
      self.salary = salary
      self.language = language
      print("I am  creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good morning")

nabeel= Employee("Nabeel",130000,"JavaScript")
# nabeel.name= "Nabeel"
print(nabeel.name, nabeel.salary, nabeel.language)