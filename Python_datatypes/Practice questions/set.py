# Q1.Find the length of a set.
'''s1 = {1,5,4}
print(len(s1))'''

# Q2.Add an element to a set.
'''s1 = {1,5,4}
s1.add(6)
print(s1)'''

# Q3.Remove an element from a set.
'''s1 = {1,5,4}
s1.remove(4)
print(s1)'''

# Q4. Find union of two sets.
'''s1 = {1,5,4,8}
s2 = {6,7,8,1,}
s3 = s1.union(s2)
print(s3)'''

# Q5. Find intersection of two sets.
'''s1 = {1,5,4,8}
s2 = {6,7,8,1,}
print(s1.intersection(s2))
'''
# Q6. Find difference of two sets.
'''s1 = {1,5,4,8}
s2 = {6,7,8,1,}
print(s1.difference(s2))'''

# Q7. Find symmetric difference of two sets.
'''s1 = {1,5,4,8}
s2 = {6,7,8,1}
print(s1.symmetric_difference(s2))'''

# Q8. Check whether an element exists in a set.
'''s1 = {1,5,4,8}
element = int(input("Enter the number:"))

if element in s1:
    print("exist")
else:
    print("Not exist")'''

# Q9.Convert a list into a set.
'''l1 = [1,2,3,4,3]
print(set(l1))'''

# Q10.Remove duplicate values from a list using a set.
'''l1 = [1,2,3,4,3]
print(set(l1))
'''
# Q11.Find common elements between two sets.
'''s1 = {1,5,4,8}
s2 = {6,7,8,1,}
print(s1.intersection(s2))'''

# Q12.Find unique elements from two sets.
'''s1 = {1,5,4,8}
s2 = {6,7,8,1}
print(s1.symmetric_difference(s2))'''

# Q13.Find largest and smallest value in a set.
'''s1 = {1,5,4,8}
print(min(s1))
print(max(s1))'''

# Q14.Find the sum of all values in a set.
'''s1 = {1,5,4,8}
print(sum(s1))'''

# Q15.Create a set from a string.
'''s1 = "hello"
print(set(s1))'''

# Q16.Find the second largest number in a set.
s1 = {1,5,4,8}
print(sorted(s1)[-2])

# Q17.Write a program to find elements present in one set but not in another.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}
print("set1:",set1-set2)
print("set2:",set2-set1)