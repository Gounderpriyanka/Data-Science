'''TAsk interchange the color name to first three character
of the second string and vice verse
input color
input full
output1 : fulor
output2 : coll'''

'''s1 = input("Enter the string:")
s2 = input("Enter the string:")
print(s2[0:3]+s1[3:])
print(s1[0:3]+s2[3:])
'''

"""Task 2 
input : Priyanka Narendran Gounder
output : P.N.Gounder
"""

# name = "Priyanka"+"Narendran"+"Gounder"
# print(name[0]+"."+name[8]+"."+name[17:])


# Task 3 : print all  "o"index number in the string
"""input : i am going to goa next month.
output : first "o" index number is 6.
         second "o" index number is 12.
         Third "o" index number is 14.
         fourth "o" index number is 
         """
'''s1 = "i am going to goa next month"
for i in range (len(s1)):
    if s1[i] == "o":
        print("index:",i)'''


# task : 2 replace second 'r' with  '#'
'''input  : restart
output  :resta#t'''

'''s1 = "restart"
count = 0
result = ""

for i in s1:
    if i == 'r':
        count += 1
        if count == 2:
            result += '#'  # Replace only the 2nd 'r'
            continue
    result += i

print(result)'''  # resta#t

# task :3 ask user to enter the string and replace first space and  last space with underscore.(_)

# input : i am going to goa next month.
# output : i_am goint to goa next_month.


c1 = "a"
c2 = "Z"
 
s = ""
for i in range(ord(c1),ord(c2)+1):
    print(s = s + chr(i) + " ")
        