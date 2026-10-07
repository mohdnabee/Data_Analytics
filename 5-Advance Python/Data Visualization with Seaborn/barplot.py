import  seaborn  as sns 
import  matplotlib.pyplot as plt 

df =  sns.load_dataset('tips')
print(df.head()) #  show as a table format  

# sns.lineplot(x= 'size' ,  y ='tip' ,  data =  df)
# plt.show()

sns.barplot(x='day' , y =  'total_bill', data = df)
plt.show()
