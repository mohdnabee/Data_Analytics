import  matplotlib.pyplot as plt
import numpy as np  

days =  np.arange(1,11) 
sales_in_cr =  np.array([1.2, 1.5, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 1.5, 5.0])

plt.figure(figsize=(10,5))
plt.style.use('fast')  # set the style of the plot
plt.plot(days , sales_in_cr , marker= 'o' ,  color = 'b' , label = 'Sales in Crores' )
plt.title('Daily Sales Over 10 Days')
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('Sales (in Crores)')
plt.savefig('daily_sales.png')
plt.show()