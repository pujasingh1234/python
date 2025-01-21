# Input a 4-digit number
number = input("Enter a 4-digit number: ")

# Initialize counters for even and odd digits
even_digits = []
odd_digits = []

# Loop through each digit of the number
for digit in number:
    # Check if the digit is even or odd
    if int(digit) % 2 == 0:
        even_digits.append(digit)
    else:
        odd_digits.append(digit)

# Print the results
print("Even digits:", even_digits)
print("Odd digits:", odd_digits)
print("Total even digits:", len(even_digits))
print("Total odd digits:", len(odd_digits))
