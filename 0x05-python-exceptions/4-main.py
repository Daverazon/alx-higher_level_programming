#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [5, 4, "j", 3]
my_l_2 = [[4, 5], 3, "j"]
result = list_division(my_l_1, my_l_2, 2)
print(result)
