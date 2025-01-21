# Input a 10-digit number
number = input("Enter a 10-digit number: ")

# Check if the input is a valid 10-digit number
if len(number) == 10 and number.isdigit():
    # Print the alternate digits (even-indexed digits)
    alternate_digits = number[::2]  # Start from index 0 and take every second digit
    print("Alternate digits:", alternate_digits)
else:
    print("Please enter a valid 10-digit number.")
