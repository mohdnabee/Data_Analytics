class Employee: 
    company = "ITC"
    def show(self): 
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer: 
#     company = "ITC Infotech"
#     def show(self): 
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self): 
#         print("The name is {self.name} and he is good at {self.language} language")

class Programmer(Employee):
      company = "ITC Infotech"
      def show(self): 
        print(f"The name is {self.name} and the salary is {self.salary}")

a=  Employee()
b= Programmer()

print(a.company , b.company)



