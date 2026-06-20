student = int(input("Enter the total student:"))
d1 = {}
for i in range (student):
    name = input("Enter the name:")
    marks = int(input("Enter the marks:"))
    d1[name] = marks
print(d1)
