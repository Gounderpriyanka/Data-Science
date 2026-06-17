total = int(input("Enter the total number:"))
l1 = []
oddsum = 0
evensum = 0
for i in range(1,total+1):
    num = int(input("enter a number:"))
    l1.append(num)
    
print("Sum",sum(l1))
for i in l1:
    if i%2==0:
        evensum +=i
    else:
        oddsum +=i
print("odd sum:",oddsum)
print("Even sum:",evensum)
        
