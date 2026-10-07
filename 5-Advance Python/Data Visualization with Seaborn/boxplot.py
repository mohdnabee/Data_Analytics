import  seaborn  as sns 
import  matplotlib.pyplot as plt 

df =  sns.load_dataset('tips')
print(df.head()) #  show as a table format  


sns.boxplot(x='day' , y =  'total_bill', data = df)
plt.show()

#   box plot  shows a mean and median of the data,  and also shows the outliers in the data.  It is a good way to visualize the distribution of the data.  It is also a good way to compare the distribution of the data across different categories.