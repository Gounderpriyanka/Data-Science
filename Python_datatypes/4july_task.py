"""
1.
Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.
For Example:-
Input:-This is the python program
Output:-No of Words=5
	    No of letters=26(including whitespace)
	    Longest Word=program

2.Ask user to give name and marks of 5 different students. Store them in dictionary.
 Sort the above dictionary in ascending order of Marks.
 
 input : {'John':90,'Tom':80,'Anna':85,'Peter':75,'Sara':60}
 output :{'Sara' :60,'Peter':75,'Tom':80,'Anna':85,'John':90}

3. sort tuple  by second element of tuple. 
input :- t = [('John', 90), ('Tom', 80), ('Anna', 85), ('Peter', 75), ('Sara', 60)]
output :- t = [('Sara', 60), ('Peter', 75), ('Tom', 80), ('Anna', 85), ('John', 90)]
"""

# word = input("Enter the sentences:")
# No_of_letters = len(word)
# longest_word = ""
# n = word.split(sep=" ")
# count = 0
# for i in range(len(n)):
#     if len(n[i]) > count:
#         count = len(n[i])
#         longest_word = n[i]
# print("No of letters:",No_of_letters)
# print("No of words:",len(n))
# print("Longest word:",longest_word)

input = {'John':90,'Tom':80,'Anna':85,'Peter':75,'Sara':60}
sorts_input = sorted(input.values())
output = {}
print(sorts_input)
for i ,j in input:
    output[i] = sorts_input[i]
print(output)
students = {'John': 90, 'Tom': 80, 'Anna': 85, 'Peter': 75, 'Sara': 60}

sorted_students = {}

# Sort the marks
sorted_marks = sorted(students.values())

# Create a new dictionary in ascending order of marks
for mark in sorted_marks:
    for name in students:
        if students[name] == mark and name not in sorted_students:
            sorted_students[name] = mark
            break

print(sorted_students)
