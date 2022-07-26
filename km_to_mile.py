# 1. Kilometers --> Miles 

#  Taking Kilometers input from user
kilometer = float(input("Enter the value of Kilometers: "))

# Conversion factor
conv_fac = 0.621371

# Calculate miles
miles = kilometer * conv_fac

# Print the result in upto two-precision value
print("%0.2f kilometers is equal to %0.2f miles" %(kilometer,miles))

# 2. Miles -->  Kilometers

# Taking Miles input from user
miles_1 = float(input("Enter the value of miles: "))

# Conversion Factor
conv_fac_1 = 1.60934

# Calculate kilometers
kilometer_1 = miles * conv_fac_1

# Print the result in upto two-precision value
print("%0.2f miles is equal to %0.2f kilometers" %(miles_1,kilometer_1)) 