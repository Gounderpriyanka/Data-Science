d1 = {"abs":23,
      "ers":45,
      "llm":32,}

print(len(d1))

# Q.13 Count frequency of characters in a string using a dictionary.


# Q.14 Create a dictionary from two lists.
'''l1 = ["abc","cdv","gsd","dsd"]
l2 = [23,56,78,53]
d1 = {}
for i in range(len(l1)):
    d1[l1[i]] = l2[i]
print(d1)'''

# Q.15 Sort a dictionary by keys.
d1 = {'abc': 23, 'cdv': 56, 'gsd': 78, 'dsd': 53}
sorted_dic ={}
for i in sorted(d1):
    sorted_dic[i] = d1[i]
print(sorted_dic)