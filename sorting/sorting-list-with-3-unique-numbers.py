# Given a list of numbers with only 3 unique numbers (1, 2, 3),
# sort the list in O(n) time.

numbers = [3, 3, 2, 1, 3, 2, 1]

list_1 = []
list_2 = []
list_3 = []
sorted_list = []

for number in numbers:
    if len(list_1) == 0:
        list_1.append(number)
    elif number == list_1[0]:
        list_1.append(number)
    elif len(list_2) == 0:
        list_2.append(number)
    elif number == list_2[0]:
        list_2.append(number)
    elif len(list_3) == 0:
        list_3.append(number)
    elif number == list_3[0]:
        list_3.append(number)

if list_1[0] < list_2[0]:
    if list_1[0] < list_3[0]:
        if list_2[0] < list_3[0]:
            sorted_list = list_1 + list_2 + list_3
        else:
            sorted_list = list_1 + list_3 + list_2
    else:
        sorted_list = list_3 + list_1 + list_2
else:
    if list_1[0] < list_3[0]:
        sorted_list = list_2 + list_1 + list_3
    elif list_2[0] < list_3[0]:
        sorted_list = list_2 + list_3 + list_1
    else:
        sorted_list = list_3 + list_2 + list_1

print(f"Input: {numbers}")
print(f"Output: {sorted_list}")

