# Input a 10-digit number
number = input("Enter a 10-digit number: ")

# Check if the input is a 10-digit number
if len(number) == 10 and number.isdigit():
    # Find the maximum digit in the number
    max_digit = max(number)
    
    # Print the maximum digit
    print("The maximum digit is:", max_digit)
else:
    print("Please enter a valid 10-digit number.")
