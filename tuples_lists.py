#Creating a tuple

tuple1 = ("Elephent", 43,12.43, True)
print(type(tuple1))
#access tuple using indexing
print(tuple1[0])
#access tuple using negative indexing
print(tuple1[-2])

#concatenate two tuples
tuple2 = ("Lion", 23, 45.32, False)
tuple_concat= tuple1 + tuple2
print(tuple_concat)

tuple_new = tuple1 + ("Giraffe", 56, 78.90, True)
print(tuple_new)

#tuples slicing 
#if we want to get multiple elements from a tuple we can use slicing
tuple_slice = ("Apple", "Mango", 12,65.434,True)
#to get first 3 elemts
print(tuple_slice[0:3])
#to get last two elements
print(tuple_slice[4:6])

#tuples are immuatble. so we can not change once it is created.
#variables are referenced to a paticular tuple

Rating = (10, 8, 9, 7, 6)
RatingSorted = sorted(Rating)
print(RatingSorted)

#Tuples can be nested

tuple_nested = ("Lion", 12.32,445,("a","b","c"))
print(tuple_nested)

#we can access the elements in the nested tuple also
print(tuple_nested[3][1])

