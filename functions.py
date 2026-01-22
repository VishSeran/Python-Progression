def Multiply(a,b):
    result = a * b
    return result

print(Multiply(5,6))
print(Multiply(2,"Hi"))# won't get error when having two types

#if function doesn't have any body then there must be have `pass` keyword otherwise it will get an error
def NoWork():
    pass

print(NoWork()) #returns `none`

def PrintArrayWithIndex(array):
    for i,element in enumerate(array):
        print(f"{i} index is having {element} value")

stuff  = ['a','b','c','d','e']
PrintArrayWithIndex(stuff)

#collection of arguments in the function
def ArtistsNames(*names):# we dont know how many names user will input
    for name in names:
        print(name)

ArtistsNames('asas','dsfd','tryt')
ArtistsNames(12,23,34,45,56,6778,78,89)

#we can make a variable global by writing `global` in front of it

def teaMake(people):
    global teacups
    teacups = 2 * people
    return teacups

print(teaMake(3))
print(teacups)
