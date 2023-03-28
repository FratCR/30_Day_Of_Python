# 30 Days of Python Lessons

# Start of Day 1

# DATA TYPES

print(type(18))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Firat'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Firat'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# OPERATORS

"""
# we can use 3 nail to the area we don't want it to detect
addition(+)
subtraction(-)
multiplication(*)
division(/)
exponential(**)
modulus(%)
Floor division operator(//)
"""

# End of the Day 1

# --------------------

# Start of the Day 2

# variable names must not start with numbers or special characters or '-' character
# No spaces when naming a variable

number1, string1, float1 = 13, "Hi Guys", 2.69 # you can add multiple value in 1 line
print("Firat saying: ", string1)

name, age = input("What is your name ? "), input("What is your age ? ") # you can want user input and you can add multiple in 1 line again
print(f"Hello {name}! Welcome to our store. Your age is {age}, right huh {name} ?")

# CONVERT TYPES

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to float
num_str = '10.6'      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Firat'
print(first_name) # 'Firat'
first_name_to_list = list(first_name)
print(first_name_to_list) # ['F', 'i', 'r', 'a', 't']

# End of the Day 2

# -------------------

# Start of the Day 3

# PYTHON OPERATORS

"""
Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3
"""

"""
Operator	Name	                    Example
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y
"""

"""
Operator	Description	                                                Example
and 	    Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
"""

# Homework 1: Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
print("Calculate the area of the triangle by entering the base area and height values (cm)")
basearea = float(input(" Enter a Base area: "))
height = float(input("Enter a Height: "))
triangleArea = (basearea * height)/2
print(f"Your Triangle area is {triangleArea} santimeters...")

# Homework 2: Find the length of 'python' and 'dragon' and make a falsy comparison statement

print(len("Python") == len("Dragon")) == False

# Homework 3: Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person

print("Enter your hourly money earnings and work hours, let's find your weekly and monthly earnings")
Rph = float(input("Enter your rate per hour: "))
daily_work = float(input("Enter your daily work hour as dollar: "))
daily_earn = (Rph * daily_work)
print("Your weekly earned money is: ", daily_earn * 7," USD$")
print("Your montly earned money is: ", daily_earn * 30, " USD$")

# End of the Day 3

# -----------------

# Start of the Day 4

