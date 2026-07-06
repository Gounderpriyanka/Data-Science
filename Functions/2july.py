
# print in lambda
'''a = lambda x: print("my name is:",x)
a ("Priyanka")
a ("sara")'''

# 
'''result = lambda a,b : print("a is big",a) if a>b else(print("b is big",b))
result(23,5)'''

#
'''r = lambda a,b,c : print(min(a,b,c))
r(1,6,89)
r1 = lambda a,b,c : print(max(a,b,c))
r1(56,23,45)
r2 = lambda a,b,c : sorted([a,b,c])
print(r2(45,89,63))'''

#
'''a = lambda x : len(x)
print(a("abcd"))
print(a([1,2,3,4,5]))
print(a({"a","b","c",45}))
print(a({"a":45,"b":23}))'''

#
'''a = lambda *x : sum(x)
print(a(1,6,56,78))
'''
# filter
'''l1=[1,2,3,4,5,6,7,8]
result = list(filter(lambda x : x%2==0,l1))
print(result)

l2={19, 65, 57, 39, 152, 639, 121, 44, 90, 190}
result = list(filter(lambda x : x%13==0,l2))
print(result)
result1 = list(filter(lambda x : x%19==0,l2))
print(result1)


l1 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
l2 = []
result = list(filter(lambda  x : x == x[::-1],l1))
print(result) '''

# map 
l1=[1,2,6,7,8]
result = list(map(lambda x : x * 5,l1))
print(result)

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result1 = list(map(lambda x : x**2,l2))
print(result1)
result2 = list(map(lambda x : x**3,l2))
print(result2)
