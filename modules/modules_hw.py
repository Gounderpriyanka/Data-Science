'''# difference  sample and choice
1. random.choice()
Purpose: Selects one random element from a sequence.
Duplicates: Not applicable (only one element is returned).
Return type: Single element (not a list).
Raises error: If the sequence is empty.

Example:
import random

items = [1, 2, 3, 4, 5]
print(random.choice(items))  # e.g., 3

2. random.sample()
Purpose: Selects multiple distinct random elements from a sequence.
Duplicates: Not allowed — all returned elements are unique.
Return type: List of elements.
Raises error: If k (sample size) > length of sequence.
Example:
import random

items = [1, 2, 3, 4, 5]
print(random.sample(items, 3))  # e.g., [4, 1, 5]

'''



import random as r 
def game():
    choice = r.randint(1,20)
    
    for i in range(1,6):
        print(f"\nChance {i}/5")
        a = int(input("Enter a number 1 to 20  :"))

        if a>choice:
            print("Enter a smallest number!")
            
        elif a<choice:
            print("Enter a gretest number!")
        else:
            print("😎 you win the game!🎉")
            break
    else:
        print("😔 You loss the game!👍")

    print(choice)
game()

'''import utils as u
u.marks()
u.calculate_percentage(98,96,78)
u.calculate_grade(90)
'''

