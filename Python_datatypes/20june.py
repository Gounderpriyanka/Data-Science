# student = int(input("Enter the total student:"))
# d1 = {}
# for i in range (student):
#     name = input("Enter the name:")
#     marks = int(input("Enter the marks:"))
#     d1[name] = marks
# print(d1)


# num = int(input("Enter the number:"))

# print("1.")
# for i in range(num,0,-1):
#     print("  "*(num-i),"* "*i,end=" ")
#     print("")

# print("2.")
# for i in range(num,0,-1):
#     print(" "*(num-i),"* "*i,end="")
#     print("")
    
# print("3.")
# for i in range(1,num+1):
#     print("  "*(num-i),"* "*i,end="")
#     print("")

# print("4.")
# for i in range(1,num+1):
#     print(" "*(num-i),"* "*i,end="")
#     print("")

# print("5.")
# for i in range(1,num+1):
#     print(" "*(num-i),"* "*i,end="")
#     print("")
# for i in range(num-1,0,-1):
#     print(" "*(num-i),"* "*i,end="")
#     print("")


#Task2
# num = int(input("Enter the total num"))
# l1 = []
# for i in range(num):
#     n = int(input("Enter the number:"))
#     l1.append(n)
# print(l1)
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
    
# print(l2)

#Task3
num = int(input("Enter the total"))
# input  : l1 =[[0,4],[1,2],[6,7]]
# output  : l1 =[[1,2],[0,4],[6,7]]
l1 = []
for i in range(num):
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    l1.append([a,b])

print(l1)

print(sorted(l1))



       
