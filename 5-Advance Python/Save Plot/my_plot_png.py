import  matplotlib.pyplot as plt 
import numpy as np 
import  matplotlib

# generate some data 
x = np.linspace(0, 10, 100)
y = np.sin(x)   


# create a plot  
plt.figure(figsize=(8,4))
plt.style.use('seaborn-v0_8-dark')  # set the style of the plot
# print(matplotlib.style.available)
#   X and Y labes 
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x, y, label = 'Sine Wave')
plt.title('Sine Wave Plot')

# plt.savefig('my_plot.png')  # save the plot as a PNG file
plt.savefig('my_plot.pdf')  # save the plot as a PNG file with higher resolution and tight layout
plt.show()