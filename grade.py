math_marks=int(input("enter marks of math:"))
eng_marks=int(input("enter marks of english:"))
if math_marks>80 and eng_marks>80:
    print("grade : A")
elif math_marks>80 or eng_marks>80:
    print("grade : B")
else :
    print("grade : C")
