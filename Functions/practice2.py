# Lambda Functions

"""
'''Q1.Write a lambda function that takes a number and returns its square.'''
result = lambda a : a**2
print(result(4))

'''Q2.Write a lambda function that takes two numbers and returns their product.'''
result = lambda a,b : a*b
print(result(3,9))

'''Q3.Write a lambda function that checks whether a given number is even, returning True or False.'''
result = lambda a : True if a%2==0 else False
print(result(4))

'''Q4.Use a lambda function as the key to sort a list of tuples by their second element.'''
students = [("Amit", 85), ("Riya", 92), ("Neha", 78), ("Karan", 88)]
result = sorted(students, key=lambda x : x[0])
print(result)

'''Q5.Write a lambda function that takes a string and returns it reversed.'''
result = lambda x : x[::-1]
print(result("hello"))

"""
"""
# Map
'''Q1.Use map() to convert a list of integers into a list of their squares.'''
l1 = [1,2,3,4,5,6]
result = list(map(lambda z : z**2,l1))
print(result)

'''Q2.Use map() to convert a list of temperatures in Celsius into Fahrenheit.'''
celsius = [0, 20, 30, 40]
result = list(map(lambda x : (x*9/5)+32,celsius))
print(result)

'''Q3.Use map() with a lambda to convert a list of strings into their lengths.'''
words = ["apple", "banana", "kiwi", "grapes"]
result = list(map(lambda x : len(x) ,words))
print(result)

'''Q4.Use map() on two lists simultaneously to add corresponding elements together.'''
list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
result = list(map(lambda x,y: x+y ,list1,list2))
print(result)

'''Q5.Use map() to convert a list of strings to uppercase.'''
names = ["priyanka", "amit", "riya", "karan"]
result = list(map(lambda x : x.upper(),names))
print(result)
"""
# Filter
"""
'''Q1. Use filter() to extract all even numbers from a list of integers.'''
numbers = [12, 7, 18, 5, 20, 9, 14]
result = list(filter(lambda x : x%2 == 0,numbers))
print(result)

'''Q2.Use filter() to extract all words longer than 4 characters from a list of strings.'''
words = ["cat", "apple", "dog", "banana", "kiwi", "orange"]
result = list(filter(lambda x : len(x)>4,words))
print(result)

'''Q3.Use filter() with a lambda to remove all None values from a list.'''
data = [10, None, "Python", None, 25, "AI", None]
result = (list(filter(lambda x : x != None,data)))
print(result)

'''Q4.Use filter() to find all numbers in a list that are divisible by both 3 and 5'''
numbers = [10, 15, 18, 30, 45, 50, 60, 75]
result = (list(filter(lambda x : x%3==0 and x%5==0,numbers)))
print(result)

'''Q5.Use filter() to extract all palindromic strings from a list of words'''
words = ["madam", "python", "level", "hello", "radar", "world", "noon"]
result = list(filter(lambda x : x[::-1]==x,words))
print(result)
"""
#Enumerate
'''Q16. Use enumerate() to print each item of a list along with its index.'''
l1 = ["apple","mango","cherry","radish","carrot"]
for i , j in enumerate(l1):
    print(i,j)

l1 = ["red","orange","abc","asd"]
d1 = {}
for i ,j in enumerate(l1):
    d1[j] = i
print(d1)

l1 = ["red","orange","abc","asd"]
for i , j in enumerate(l1,start=1):
    print(i,":",j)

l1 = [12,25,-8,15,-4]
for i , j in enumerate(l1):
    if j<0:
        print(i)
        break

l1 = ["Apple", "Mango"," Banana"," Orange ","Grapes"]
for i, j in enumerate(l1):
    if i%2==0:
        print(j)


