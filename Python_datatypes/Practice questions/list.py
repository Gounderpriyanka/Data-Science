# Question-1
'''l1 = [6,78,56,89,35,33]
print(len(l1))'''

# Question-2
'''l1 = [6,78,56,89,35,33]
print(l1)
print(l1[::-1])'''

# Question 3
'''l1 = [6,78,56,89,33,35,33]
print(l1)
print(l1.count(6))'''

# Question 4
'''l1 = [6,78,56,89,35,33]
print(l1)
print(l1.index(78))'''

# Question 5
'''l1 = [6,78,56,89,35,33]
print(max(l1))
print(min(l1))'''

# Question 6
'''l1 = [6,78,56,89,35,33]
print(l1.append(7))
print(l1)
'''

# Question 7
'''l1 = [6,78,56,89,35,33]
l1.insert(1,88)
print(l1)'''

# Question 8
'''l1 = [6,78,56,89,35,33]
print(l1)
l1.remove(6)
print(l1)'''

# Question 9
'''l1 = [6,78,56,89,35,33]
print(l1)
print(sorted(l1))'''

# Question 10
'''l1 = [6,78,56,89,35,33]

print(sorted(l1,reverse = True))'''

# Question 11
'''l1 = [6,78,56,89,35,33,45,45,78,6,2]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)'''

# Question 12
'''l1 = [6,78,56,89,35,33]
l2 = [45,88,63,2,6,56]
l1.extend(l2)
print(l2)
'''
# Question 13
'''l1 = [6,78,56,89,35,33]
l2 = [45,88,63,2,6,56]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)'''

# Question 14
'''l1 = [6,78,56,89,35,33]
print(sum(l1))'''

# Question 15
l1 = [6,78,56,89,35,33]
even = []
odd = []
for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)