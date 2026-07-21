"""
create  a new module 

1.utils.py
    function  : 1. calculation of  percent 
    function  : 2. calculation of  grade 
    function  : 3. enter the  3 subject marks 
2.main.py
"""

def marks():
    science = int(input("Enter a science marks:"))
    maths = int(input("Enter a maths marks:"))
    english = int(input(" Enter a english marks:"))
    return science,maths,english

def calculate_percentage(science,maths,english):
    percentage = (science+maths+english)/3
    return print("Percentage: ",percentage)

def calculate_grade(percentage):
    if percentage>=90:
        print("Grade A+")
    elif percentage>=80:
        print("Grade A")
    elif percentage>=70:
        print("Grade B+")
    elif percentage>=60:
        print("Grade B")
    elif percentage>=50:
        print("Grade C+")
    else:
        print("Fail")




