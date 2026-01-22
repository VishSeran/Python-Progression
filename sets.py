#unless lists and tuples, the sets doesn't have ordered sequence
# sets only have a unique elements, no duplicate items

#we can input a list to **set()** and make the list to a set

list1 = ['abc',3,4,5.43,True,3,3,4]
print(list1)

set1 = set(list1)
print(set1)

# set operations

#add an item
set1.add('you')
print(set1)

#remove an item
set1.remove('abc')
print(set1)

#verify elements
check = 3 in set1
print(check)

#for set interdection we use '&'
album1 = {'you','I',1,2,3.5,('apple',True)}
print(album1)
album2 = {2,3.5,('apple',True),100,10000,25}
print(album2)

set_intersect = album1 & album2
print(set_intersect)

#union of sets
set_union=album1.union(album2)
print(f"set union: {set_union}")

#SUBSET of a set
album3 = {100,10000,25}
print(album3.issubset(album2))


