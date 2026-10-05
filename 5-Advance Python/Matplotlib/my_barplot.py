import  matplotlib.pyplot as plt 
import  numpy  as np  


categories = ["A" ,"B" ,"C"]
values = [12,44,53]

plt.bar (categories ,  values)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show ()

