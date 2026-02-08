import numpy as np 
import pandas as pd  

## series using list
countries = ['India', 'USA', 'Canada', 'Nepal']
table = pd.Series(countries)
print(table) 

# custom index 

subjects = ['math', 'english', 'hindi']
marks = [1,2,3]
table1  = pd.Series(marks, index=subjects, name='student marks') 
print(table1)


## series using dictionaries 

marks1 = {
    'math' : 1,
    'english': 2,
    'science' : 3, #
    'sst': 3
}
table2 = pd.Series(marks1, name='student marks')
print(table2)


## series Attributes 
# size , dtype, name , ,is_unique , index, values,

print(table2.size)
print(table2.name)
print(table2.dtype)
print(table2.is_unique)
print(table2.index)
print(table2.values) 


## csv explicitly gives data frame we convert it to series using squeeze
df = pd.read_csv("subs.csv")
s= df.squeeze()
print(type(s))
print(s)

df1 = pd.read_csv("kohli_ipl.csv", index_col= 'match_no')
s1 = df1.squeeze()
print(type(s1))
print(s1)


df2 = pd.read_csv("bollywood.csv" , index_col='movie')
s2 = df2.squeeze()
print(type(s2))
print(s2)



