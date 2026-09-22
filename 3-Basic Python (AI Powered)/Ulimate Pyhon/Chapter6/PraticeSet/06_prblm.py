# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F

marks =  int (input("Enter your marks: "))

if(marks <= 100 and marks >= 90):
    grade = "EX"
elif(marks<90 and marks>=80):
    garde="A"
elif(marks<80 and marks>=70):
    garde="B"
elif(marks<70 and marks>=60):
    garde="C"
elif(marks<=0 and marks>=50):
    garde="D"
elif(marks<50 ):
    garde="F"

print("your grade is: ", garde)
