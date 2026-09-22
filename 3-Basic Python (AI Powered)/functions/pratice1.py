def salary  (salary , name =""  ,  Department  = " "  ): 
    bonus = salary  *  10  /  100  #  10 %  BOUNUS  
    print(f"Mr {name} your bonus is { bonus} and deparmnt  is {Department} " )
    print (f"total  salary =  {salary + bonus} \n")

salary(salary= 50000 , name = "Nabeel" ,  Department= "CSE")
salary(salary= 60000 , name = "Tusahr" ,  Department= "IT")
salary(salary= 45000 , name = "Ketan" ,  Department= "CS")

