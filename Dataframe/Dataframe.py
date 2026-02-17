import pandas as pd

data = [10,20,30,40,50,60,70]
s = pd.Series(data)
print(s)

##Access by label(index)
print(s[2])

##Access by position
print(s.iloc[2])

##Access multiple elements
print(s[1:4]) ## last index not showing

##Creating DataFrames from Dictionaries:

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)
print(df[['Name','Age']]) ##print df columns

##access rows by label(index) -> loc and position ->iloc

## by index/label
print(df.loc[1]) ## row in index 1
print(df.loc[1:2]) ## row range in index 1 and 2

## by position
print(df.iloc[2]) ## row in position 1
print(df.iloc[0:1]) ## row range in position 0 and 1

## unique data
unique_df = df['Age'].unique()
print (unique_df)

## conditional filtering
high_above_25 = df[df['Age'] >25]
print(high_above_25)

high_above_25.to_csv("filter_data.csv")
