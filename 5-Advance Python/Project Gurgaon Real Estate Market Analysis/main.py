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
# print(df.info())

# Question 1 : Which is the costliest flat in the dataset?
costliest_flat  =  df.loc[df['price'].idxmax()]
# print(costliest_flat)
print(f"The costliest  flat  is a {costliest_flat['bhk_count']} BHK flat located in  {costliest_flat['locality']} priced at {costliest_flat['price'] /10000000  } crores  in  {costliest_flat['society']} society.  " )

# Question 2 Which locality has the highest average price?
higest_avg_price_locality = df.groupby("locality")["price"].mean().idxmax()
print (f'The locality  with  the highest  average price is {higest_avg_price_locality}  ')

#   Question 3 Which locality has the highest rate per square foot?
highest_rate_locality =  df.groupby('locality')['rate_per_sqft'].mean().idxmax()

print(f"The locality with the higest rate per square foot is {highest_rate_locality} ")


# Question 4 .  Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price  =  df [df['status'] ==  'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under-construction']['price'].mean()

if ready_to_move_avg_price >  under_construction_avg_price : 
    print("Ready-to-move properties cost  more on average then  under-construction  properties.")
else: 
    print("Under-construction properties cost  more on average then reay-to-move properties.")

# Question 5 .  Do RERA-approved properties command a price premium?

rera_approved_avg_price =  df[df['rera_approval']== True]['price'].mean()
rera_not_approved_avg_price =  df[df['rera_approval'] ==  False]['price'].mean()

if rera_approved_avg_price >  rera_not_approved_avg_price : 
    print ("RERA-approved properties command a price  premium.")
else : 
    print ("RERA-approved properties do  not command a price premium.")


#Question 6 .  How does area (sqft) impact property price?

# sns.scatterplot(data =  df ,  x ='area' ,  y = 'price')
# plt.show()



#Question 7 .  Which BHK configuration is the most expensive on average?
most_expensive_bhk =  df.groupby("bhk_count")["rate_per_sqft"].mean().idxmax()
print(f'The most expensive BHK  configuration  on average is {most_expensive_bhk} BHK.') 



# Question 8 .   Which property type (Apartment, Floor, Plot) is the costliest?

most_expensive_property_type =  df.groupby("flat_type")["price"].mean().idxmax ()
print (f"the most expensive property  type is  {most_expensive_property_type}.")

#Question 9 .  Do certain builders or companies consistently price higher?

print (df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending= False).head(5))
# print name of top  5 

print ("The Top  5 buliders that  price higher are: ")
top_5_builders =  df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending= False).head(5)
for builder  in  top_5_builders.index: 
    print(builder,  end= ", ")


# Question 10 .  Are larger homes always more expensive per square foot ?


sns.scatterplot(data= df ,  x='area' , y ='rate_per_sqft')
plt.show()