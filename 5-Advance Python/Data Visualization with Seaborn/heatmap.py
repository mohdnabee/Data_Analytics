import  seaborn  as sns 
import  matplotlib.pyplot as plt 

df =  sns.load_dataset('tips')
print(df.head()) #  show as a table format  
sns.heatmap(df.corr(numeric_only=True) ,  annot=True) 
plt.show()

