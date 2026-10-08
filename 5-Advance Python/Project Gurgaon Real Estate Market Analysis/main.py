import  pandas  as pd 
import  matplotlib.pyplot  as plt
import  seaborn  as sns

df =  pd.read_csv('data.csv')
# print(df.head())
# print(df.columns.tolist())

# print(df.info())

#   Data Cleaning 

df.columns =  df.columns.str.strip().str.lower().str.replace(' ', '_')
# print(df.columns.tolist())

df = df.drop_duplicates()


#   Numerical  Columns Cleaning

df['price'] =  df["price"].astype(str).str.replace("," , "") .astype(float)

df['area'] =  df["area"].astype(str).str.replace("," , "") .astype(int)


df['rate_per_sqft'] =  df["rate_per_sqft"].astype(str).str.replace("," , "") .astype(int)

# print (df['rate_per_sqft'])

#  Categorical  Columns Cleaning 
df['status'] =  df  ['status'].str.strip().str.lower()
df['rera_approval'] =  df['rera_approval'].str.strip().str.lower().map({'approved by rera' : True , 'not approved by rera': False })
df['flat_type'] =  df['flat_type'].str.strip().str.lower()

df =  df.drop_duplicates()

# print(df)
print(df.info())