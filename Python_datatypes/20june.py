# student = int(input("Enter the total student:"))
# d1 = {}
# for i in range (student):
#     name = input("Enter the name:")
#     marks = int(input("Enter the marks:"))
#     d1[name] = marks
# print(d1)

# Task1
num = int(input("Enter the number:"))
for i in range(num+1):
                                        
     for j in range(i):
        print("*",end="")

     print("") 

#task2
num = int(input("Enter the number:"))
for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print("") 

#task3
num = int(input("Enter the number:"))
for i in range(num,0,-1):
    print(" "*(num-i),end="")
    for j in range(i):
        print("*",end="")
    print("")

#task4
num = int(input("Enter the number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(i):
    
        print("*",end="")
        # print(""*(num-i),end="") 
    print("")    

num = int(input("Enter the number:"))
for i in range(num,1,-1):
    for j in range(i):
        print(" "*(num-1),"*",end="")
    print("")         

