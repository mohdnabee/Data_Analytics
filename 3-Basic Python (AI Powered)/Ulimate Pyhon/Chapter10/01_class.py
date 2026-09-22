class Employee :
    # name = "Nabeel"
    language = "Py" # This is a class attribute
    salary= 1200000

nabeel = Employee()
nabeel.name  ="Nabeel"# This is an instance attribute
print(nabeel.name, nabeel.language , nabeel.salary)

rohan = Employee()
rohan.name = "Rohan Roro"
print(rohan.name, rohan.salary, rohan.language )

#  Here name is instance attribute and language and salary are class attributes. as they  directly belong to the class 
