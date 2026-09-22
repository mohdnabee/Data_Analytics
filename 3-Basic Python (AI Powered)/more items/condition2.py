salary = int(input("Enter Your Salary: "))

if salary >= 100000:
    bonus = salary * 0.30
elif salary >= 70000:
    bonus = salary * 0.20
elif salary >= 50000:
    bonus = salary * 0.15
elif salary >= 30000:
    bonus = salary * 0.10
else:
    bonus = 0

print(f"Your Bonus is ₹{bonus:.2f}")
print(f"Your Total Salary is ₹{salary + bonus:.2f}")