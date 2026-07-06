'''1. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''

# l1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# result = sorted(l1, key=lambda x : x[1])
# print(result)

'''2. Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

# l1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
#       {'make': 'Mi Max','model': '2', 'color': 'Gold'}, 
#       {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# result = sorted(l1,key=lambda x : x[""])
# print(result)



'''3. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.

Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight > 70kg:
output : {'Cierra Vega': (6.2, 70)}
'''
# d1 = {'Cierra Vega': (6.2, 70),
#         'Alden Cantrell': (6.3, 71),
#         'Kierra Gentry': (6.0, 68),
#         'Pierre Cox': (5.8, 66)}
# result = dict(filter(lambda x : x[1][0] > 6 and x[1][1]>=70 ,d1.items() ))
# print(result)

'''4. Write a Python program to remove all elements from a given list present in another list using lambda.

Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]'''

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2, 4, 6, 8]
# result = list(filter(lambda x : x not in list2,list1))
# print(result)

'''5. Write a Python program to reverse strings in a given list of string values using lambda.

Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']'''

# l1 = ['Red', 'Green', 'Blue', 'White', 'Black']
# result = list(map(lambda x : x[::-1],l1))
# print(result)