'''# 1. Maximum of Three Numbers
# Write a Python function to find the maximum of three numbers.

def maxi(a,b,c):
    # a = int(input("Enter a  first number:"))
    # b = int(input("Enter a second number:"))
    # c = int(input("Enter a third number:"))

    if a>b:
        if a>c:
            print("a is the maximum number",a)
    elif b>c:
        if b>a:
            print("b is the maximum number:",b)
    else:
        print("c is the maximum number:",c)
d = maxi(12,53,66)'''


'''# 2. Sum All Numbers in a List
# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def total(a):
     return"The sum of all the numbers:",sum(a)

l1 = [8,2,3,0,7]
print(total(l1))'''

'''# 3. Multiply All Numbers in a List

# Write a Python function to multiply all the numbers in a list.

# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multi(a):
    b = 1
    for i in a :
        b *=i
    print("the numbers multiplyed:",b)
l1 = [8, 2, 3, -1, 7]
multi(l1)
'''

'''# 4. Reverse a String
# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse(a):
    
    reversedd = a[::-1]
    print(reversedd)
Sample_String = "1234abcd"
reverse(Sample_String)'''

'''# 5. Factorial of a Number
# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def fact(a):
    c = 1
    for i in range(1,a+1):
        c *=i
    print(c)
fact(5)
'''

'''# 6. Check if a Number Falls Within a Given Range
# Write a Python function to check whether a number falls within a given range.

def fall():
    a = int(input("Enter a number:"))
    b = int(input("Enter the starting number:"))
    c = int(input("Enter the ending number:"))
    
    if a>=b and a<=c:
            print("The number in the range")
    else:
            print("The number is not in the range:")

fall()'''

'''# 7. Count Uppercase and Lowercase Letters in a String
# Write a Python function that accepts a string and counts the number of upper and lower case letters. Educational Resources
# Discover more
# Psychology
# Dictionaries & Encyclopedias
# Data Management
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# Click me to see the sample solution

def strr(a):
    for i in a:
        count_1 = 0
        count_2 = 0
        if "A"<=i<="Z":
            count_1 +=1
        elif "a"<=i<="z":
            count_2 +=1
    print("No. of Upper case characters :",count_1)
    print("No. of Lower case Characters : ",count_2)


str1 = "Dictionaries & Encyclopedias"
strr(str1)'''

'''# 8. Return a New List with Distinct Elements from a List
# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def ditt(a):
    l1 = []
    for i in a:
        if i not in l1:
            l1.append(i)
    print(l1)
l2 = [1,2,3,3,3,3,4,5]
ditt(l2)'''


'''# 9. Check Whether a Number is Prime
# Write a Python function that takes a number as a parameter and checks whether the 
# number is prime or not. Mathematics
# Note : A prime number (or a prime) is a natural number greater than 1 and that has
# no positive divisors other than 1 and itself.

def prime(a):
    count = 0
    for i in range(1,a+1):
        
        if a%i==0:
            count +=1
    if count == 1:
            print("The number is prime:",a)
    elif count>2:
            print("The number is not prime:",a)
    else:
            print("The number is prime:",a)

prime(1)'''


'''# 10. Print Even Numbers from a Given List
# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = []
def num(a):
    for i in a:
        if i%2==0:
            l2.append(i)
    print(l2)
num(l1)'''

# 11. Check if a Number is Perfect
# Write a Python function to check whether a number is "Perfect" or not. Scripting Languages

n = int(input("Enter a number:"))

def num(a):
    l1 = []
    for i in range(1,a+1):
        if a%i == 0:
            l1.append(i)
    l1.pop()
    summ = sum(l1)
    if summ == a:
        print(a,"is a Perfect number!")
    else:
        print(a,"is not a perfect number")
    print(l1)

num(n)

'''# 12. Check if a String is a Palindrome
# Write a Python function that checks whether a passed string is a palindrome or not.


def num(a):
    rev = a[::-1]
    if rev == a:
        print("its palindrome")
    else:
        print("its not palindrome")        
st = "mom"
num(st)'''


'''# 13. Check if a String is a Pangram
# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

a = "The quick brown fox jumps over the lazy dog"
b = "python programming"

def word(a):
    a1 = a.lower()
    b = "abcdefghijklmnopqrstuvwxyz"
    for i in b:
        if i not in a1:
            print("not pangram")
            return
    print("pangram")

word(a)
word(b)
'''
