'''
Basic Operations in Pyton are :- 
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers


'''
# Store input numbers


num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")

# Add two numbers
sum = float(num1) + float(num2)

# Subtract two numbers
subtract = float(num1) - float(num2)

# Multiply two numbers
multiplication = float(num1) * float(num2)

# Divide two numbers
division = float(num1) / float(num2)

# Display the addition
print('The Addition of {0} and {1} is {2} '.format(num1, num2, sum))

# Display the subtraction
print('The subtraction of {0} and {1} is {2} '.format(num1,num2,subtract))

# Display the multiplication
print('The multiplication of {0} and {1} is {2} '.format(num1,num2,multiplication))

# Display the division
print('The division of {0} and {1} is {2} '.format(num1,num2,division))
