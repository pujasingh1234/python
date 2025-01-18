# 3. Calculate the sum of first n natural numbers
n = int(input("Enter a number to find the sum of first n natural numbers: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print(f"The sum of the first {n} natural numbers is: {sum_n}")
