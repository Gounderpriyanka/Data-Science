
# Question 1. Find the length of a tuple
'''t1 =  (12,45,36,45,78)
print(len(t1))'''

# Question 2. Reverse a tuple using slicing
'''t1 =  (12,45,36,45,78)
print(t1[::-1])
'''
# Question 3. Count occurrence of a value
'''t1 = (12,45,36,45,78)
print(t1.count(45))'''

# Question 4. Find index of an element
'''t1 = (12,45,36,45,78)
print(t1.index(45))'''

# Question 5. Find largest and smallest value
'''t1 = (45,78,23,12,89,66)
print(min(t1))
print(max(t1))
'''

# Question 6. Write a program to find duplicate values in a tuple.
'''t1 = (12,45,36,45,78)
l1 = []
for i in t1:
    if t1.count(i)>1 and not l1 :
        l1.append(i)
print(t1)
print(l1)'''

# Question 7.Find second largest number in a tuple 
'''t = (12,45,78,23,90,56)
sorted_number = sorted(t)
print(sorted_number[-2])'''

