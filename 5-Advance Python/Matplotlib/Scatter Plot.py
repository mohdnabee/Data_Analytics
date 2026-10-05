import  matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [10, 20, 15, 25, 30]

plt.style.use ('ggplot')


plt.scatter(x,y , s =100, c=  "green",  alpha =  0.3,   )
plt.title("Scatter Plot")
plt.xlabel("X-axis")    
plt.ylabel("Y-axis")
plt.show()
