'''  ask user to enter the string and separate  the  vowel and consonant in separate file .
input  : my name is meghpreet.

output : vowel.txt : 
        consonant.txt :'''

input = input("Enter the sentence:")
vowel = "" 
consonant = ""
for i in input:
    if i in "aeiouAEIOU":
        vowel+=i
    else:
        consonant +=i
print(vowel)
print(consonant)

with open("vowel.txt",'w') as f:
    f.write(vowel)

with open("consonant.txt",'w') as f:
    f.write(consonant)


    
    
