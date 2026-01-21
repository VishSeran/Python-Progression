#list are also ordered sequence
#but lists are mutable
#lists can contain floats, integers, strings, nested lists

list1 = ["Lion",12,23.43,"a",[True, False,21]]
print(list1)

#slicing also can be applied same as the tuples.
#lists can be append, extend, prepend

list2 = ["Elephant", 43, 12.43, True]

list1.extend(list2)
print(f"extend list2 to list1: {list1}")
list1.append(list2)
print(f"append list2 to list1: {list1}")

#delete element
del(list1[2])
print(list1)

del(list2[0:2])
print(list2)

print("A<C<V<B<G".split("<"))

#clone the list
list_clone = list1[:]
print(list_clone)

print([1,2,3] + [4,5,6])