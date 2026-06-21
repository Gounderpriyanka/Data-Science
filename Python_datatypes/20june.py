# student = int(input("Enter the total student:"))
# d1 = {}
# for i in range (student):
#     name = input("Enter the name:")
#     marks = int(input("Enter the marks:"))
#     d1[name] = marks
# print(d1)


num = int(input("Enter the number:"))

print("1.")
for i in range(num,0,-1):
    print("  "*(num-i),"* "*i,end=" ")
    print("")

print("2.")
for i in range(num,0,-1):
    print(" "*(num-i),"* "*i,end="")
    print("")
    
print("3.")
for i in range(1,num+1):
    print("  "*(num-i),"* "*i,end="")
    print("")

print("4.")
for i in range(1,num+1):
    print(" "*(num-i),"* "*i,end="")
    print("")

print("5.")
for i in range(1,num+1):
    print(" "*(num-i),"* "*i,end="")
    print("")
for i in range(num-1,0,-1):
    print(" "*(num-i),"* "*i,end="")
    print("")