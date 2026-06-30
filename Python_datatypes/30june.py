"""
count the numbers of vowels in a string.
count the numbers of the spaces in the string.
Reverse the string.
"""

'''a = input("Enter the string:")
s = ["a","e","i","o","u"]
l = a.lower()
count = 0
for i in s:
    for j in l:
        if i==j:
            count +=1
print(count)'''

'''a = input("Enter the sentence:")
s  = " "
count = 0
for i in a:
    if i == s:
        count+=1

print(count)'''

'''a = input("Enter a text:")
l = a[::-1]
print(l)
'''
l1 = ["1221","abc","php","aba","xyz","abca"]
"condition : first letter or last letter or digit are same and lenght is more than 3"
l2 = []
for i in l1:
    first = i[0]
    last  = i[-1]
    if first == last and len(i)>=3:
        l2.append(i)
print(l2)