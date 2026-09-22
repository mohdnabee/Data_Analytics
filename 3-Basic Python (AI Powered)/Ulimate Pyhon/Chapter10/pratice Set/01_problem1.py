class Programmer: 
    company = "Microsoft"
    def __init__(self,name, salary,pin):
       self.name =  name
       self.salary = salary
       self.pin = pin


p = Programmer("Nabeel",1200000, 482000)
print(p.name , p.salary,p.pin,p.company)

r= Programmer("Rohan",120000, 482003)
print(r.name , r.salary,r.pin,r.company)