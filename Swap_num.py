# To take input from users
x = input("Enter first number: ")
y = input("Enter second number: ")

# Print the value before swapping
print("The value of x before swapping: ", x)
print("The value of y before swapping: ", y)

# Create a temporary variable and swap the numbers
temp = x
x = y 
y = temp

# Print the values after swapping
print("The value of x after swapping: ", x)
print("The value of y after swapping: ", y)