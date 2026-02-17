import pandas as pd

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)
print(df)

x = df[['ID']]
print(x)
print(type(x))##Let's use the type() function and check the type of the variable.

#Let us retrieve the data for Department, Salary and ID columns

z = df[['Department', 'Salary', 'ID']]
print(z)


a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}


df_new = pd.DataFrame(a)
print("\n")
print(df_new)

#Problem 2: Retrieve the Marks column and assign it to a variable b

b = df_new[['Marks']]
print("\n", b)

#Problem 3: Retrieve the Country and Course columns and assign it to a variable c
c = df_new[['Country','Course']]
print("\n", c)

# Get the Student column as a series Object
df_student = df_new['Student'] ## when series of object use single square bracket only
print("\n",df_student)

'''loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. 
This method includes the last element of the range passed in it.'''

'''iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. 
This method does not include the last element of the range passed in it.'''

# Access the value on the first row and the first column using loc
print(df_new.loc[0, 'Student']) ##have to pass the name of the row or column

# Access the value on the first row and the first column using iloc
print(df_new.iloc[0,0]) #have to pass an integer index

## Access the value on the first row and the third column
print(df_new.iloc[0,2])

## Access the column using the name
print(df_new.loc[0,'Marks'])

df2 = df_new
df2 = df2.set_index("Student")
print(df2)

print(df2.loc['David','Country'])
print(df2.head())

# let us do the slicing using old dataframe df_new
print(df_new.iloc[0:2,2:4])

# let us do the slicing using old dataframe df
print(df_new.loc[0:2,'Student':'Course'])