# List of even digits
even_digits = ['0', '2', '4', '6', '8']

# Loop through numbers between 1000 and 3000
for number in range(1000, 3001):
    # Convert the number to a string to check each digit
    str_number = str(number)
    
    # Check if all digits of the number are even
    if all(digit in even_digits for digit in str_number):
        print(number)
