##try and except format
try:
    
    result = 10 / 0
except ZeroDivisionError:
    print("You cant divide by zero")
    
else:
    
    print("Successfull!")


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