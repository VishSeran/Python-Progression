##try and except format
try:
    
    result = 10 / 0
except ZeroDivisionError:
    print("You cant divide by zero")
    
else:
    
    print("Successfull!")
    

##ZeroDivisionError
def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
# Test case
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator))


##ValueError
import math
#Type your code here
def safe_root(number):
    try:
        result = math.sqrt(number)
        return result
    except ValueError:
        print('Invalid input! Please enter a positive integer or a float value.')
    finally:
        print('Result: ', result)

safe_root(5)
safe_root(-5)

##Handling Generic Exception
def complex_maths(number):
    
    try:
        result = result / (result-5)
        return result

    except Exception as e:
        print("An error occurred during calculation.")

user_input = float(input('Enter a number: '))
complex_maths(user_input)

complex_maths(2)
        