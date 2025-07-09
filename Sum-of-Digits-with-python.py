# Get input for number
num = int(input("Please enter a number: "))

# Define sum-of-digits and use "for"
sum_of_digits = sum(int(digit) for digit in str(num))

# Output the result
print(f"The sum of the digits is: {sum_of_digits}")