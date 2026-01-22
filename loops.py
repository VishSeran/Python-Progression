#for loop

for i in range(10,100):
    i = i+1
    print(i)

squares = ['red','green','orange']

for square in squares:
    print(square)
    
    
#using enumerate we can exract the index 'i' and the value     
for i, square in enumerate (squares):
    print(f"the index: {i} and the value: {square}")
    
#while loop
fruits = ['apple', 'orange','apple','apple','mango']

fruits_list = []
i = 0

while (fruits[i] == 'apple'):
    fruits_list.append(fruits[i])
    i = i + 1
    
print(fruits_list)

i = 0
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers_grater = []

while (numbers[i] <7):
    numbers_grater.append(numbers[i])
    i = i + 1
print(numbers_grater)

