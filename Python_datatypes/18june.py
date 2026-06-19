# Task1
# total =int(input("Enter the Total number:"))
# l1 = []
# for i in range (total):
#     num = int(input("Enter the number:"))
#     l1.append(num)
# sorted_l1 = sorted(l1)
# second_largest = sorted_l1[-2]
# print("List:",l1)
# print("The second Largest number is :",second_largest)

#Task 2
# total =int(input("Enter the Total number:"))
# l1 = []
# l2 = []
# for i in range (total):
#     num = int(input("Enter the number:"))
#     l1.append(num)

# for i in l1:
#     c = 0
#     for j in range(1,i+1):
#         if i%j==0:
#             c = c+1
#     if c == 2:
#         l2.append(i)

# print(l1)
# print(l2)
    
# Task3
total =int(input("Enter the Total number:"))
l1 = []
l2 = []
for i in range (total):
    num = int(input("Enter the number:"))
    l1.append(num)

for i in range (num+1):
    reverse = 0 
    for j in l1:
        temp = j   
        r = i%10
        reverse = reverse+r*10
    if reverse == temp :
        l2.append(j)

print(l1)
print(l2)       