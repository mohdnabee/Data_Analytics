import  seaborn  as sns 
import  matplotlib.pyplot as plt 

df =  sns.load_dataset('tips')
# print(df.head()) #  show as a table format  

sns.scatterplot(x='total_bill', y='tip', data=df, hue ='size')
plt.show()