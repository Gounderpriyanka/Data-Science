'''  ask user to enter the string and separate  the  vowel and consonant in separate file .
input  : my name is meghpreet.

output : vowel.txt : 
        consonant.txt :'''

# input = input("Enter the sentence:")
# vowel = "" 
# consonant = ""
# for i in input:
#     if i in "aeiouAEIOU":
#         vowel+=i
#     else:
#         consonant +=i
# print(vowel)
# print(consonant)

# with open("vowel.txt",'w') as f:
#     f.write(vowel)

# with open("consonant.txt",'w') as f:
#     f.write(consonant)


'''task :1 Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file  friends.txt.

Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !'''


def display_oddLines():

    with open("Friends.txt",'r') as f:
        content = f.readlines()
    for i in range(len(content)):
        if i%2!=0:
            print(content[i])

r = display_oddLines()


'''task :2 Write a Python program to read a text file and do following: 
1. Print no. of words 
2. Print no. statements''' 


with open("Friends.txt",'r') as f:
        content = f.readlines()
        print(len(content[1]))
num = 0
for i in range(len(content)):
        first_line = content[i]
        num += len(first_line)

print(num)