# GETTING VALUES/INPUTS FROM USER
# We use input() function to get values from the user
# int(), float(), str() function forces values entered to be of a desired data types -> Read on Type Casting

number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: ")) # the user input forced to be of a string type NB)) Recommended

sum = number1 + number2

print(f'The sum of {number1} and {number2} is {sum}')
