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
d1 = {"abs":23,
      "ers":45,
      "llm":32}
d1.pop("ers")
print(d1)

# Q.6 Get all keys from a dictionary.
d1 = {"abs":23,
      "ers":45,
      "llm":32}
print(d1.keys())

#  Q.
# Q.13 Count frequency of characters in a string using a dictionary.


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

