'''
Write a Python program that checks whether a user-entered number is positive, negative, or
zero using Boolean expressions.
'''
print("enter a number to check thw number is positive or negative")
num=int(input("ENter a number:"))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("Zero")