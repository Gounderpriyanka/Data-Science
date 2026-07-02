# Q.1 Find the length of a dictionary.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32,}
      print(len(d1))
'''

# Q.2 Access a value using a key.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32,}
print(d1['ers'])'''

# Q.3  Add a new key-value pair.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
d1["rss"] = 67
print(d1)'''

# Q.4 Update an existing value.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
d1["ers"] = 67
print(d1)'''

# Q.5  Delete a key-value pair.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
d1.pop("ers")
print(d1)
'''
# Q.6 Get all keys from a dictionary.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
print(d1.keys())'''

#  Q.7 Get all values from a dictionary.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
print(d1.values())'''

# Q.8 Get all key-value pairs.
"""d1 = {"abs":23,
      "ers":45,
      "llm":32}
print(d1)
"""
# Q.9 Check whether a key exists or not.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
key = input("Enter a key to check:")
if key in d1:
    print("Yes")
else:
    print("no")'''

# Q.10 Merge two dictionaries.
'''d1 = {"abs":23,
      "ers":45,
      "llm":32}
d2 = { "phy":45,
       "math":78,
       "chemis":63}
print(d1.update(d2))
print(d1)
'''

# Q.11 Find the key having the maximum value.
'''d2 = { "phy":45,
       "math":78,
       "chemis":63}
print(max(d2))'''

# Q.12 Find the key having the minimum value.
d2 = {"phy":45,
      "math":78,
      "chemistry":63}
print(min(d2))



# Q.13 Count frequency of characters in a string using a dictionary.
'''s1 = "mississappi"
d1 = {}
for i in s1:
    count = 0
    for j in s1:
        if i ==j:
            count +=1
    d1[i] = count
print(d1)
'''

# Q.14 Create a dictionary from two lists.
'''l1 = ["abc","cdv","gsd","dsd"]
l2 = [23,56,78,53]
d1 = {}
for i in range(len(l1)):
    d1[l1[i]] = l2[i]
print(d1)'''

# Q.15 Sort a dictionary by keys.
'''d1 = {'abc': 23, 'cdv': 56, 'gsd': 78, 'dsd': 53}
sorted_dic1 = {sorted(d1)}
sorted_dic = {}
for i in sorted(d1):
    sorted_dic[i] = d1[i]
print(sorted_dic)
print(sorted_dic1)'''

# Q.16 Write a program to find duplicate values in a dictionary.
