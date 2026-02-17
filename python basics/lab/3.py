'''
Design a program using an if statement to verify if a student is eligible for an exam based on
attendance percentage.
'''
print(" checking your percentage for exam eligibility")
per = float(input("Enter your percentage to verify the eligible or not for writing the exam:"))

if per > 70.0 and per <=100.0:
    print("You are eligible for exam")
else:
    print("you are not eligible for exam")