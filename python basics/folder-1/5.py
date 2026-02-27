'''
Construct a program that identifies the largest of three numbers 
using nested if statements.
'''
a = int(input("Enter your first number:_"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:-"))

if a > b:
    if a > c:
        print(f"{a} is large number than {b} and {c}")
    else:
        print(f"{c} is large number than {a} and {b}")
else:
    print(f"{b} is large number among {a} and {b}")
