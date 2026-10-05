import  matplotlib.pyplot as plt 
import  numpy  as np  

sizes  =  [40 , 36 , 28 ]
labels = ["XXL" ,"XL" ,"XS"]

plt.pie(sizes , labels =  labels ,  autopct = '%d%%' , )
plt.show()