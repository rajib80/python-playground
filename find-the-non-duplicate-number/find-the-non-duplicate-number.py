# Given a list of numbers, where every number shows up twice except for one number, 
# find that one number.

def find_single_number(numbers):
    result = numbers[0]
    print(result)
    for i in range(1, len(numbers)):
        result = result ^ numbers[i]
        print(result)
    
    return result


input_numbers = [4, 3, 2, 4, 1, 3, 2]
print("Element occuring once is", find_single_number(input_numbers))

input_numbers = [2, 3, 5, 4, 5, 3, 4] 
print("Element occuring once is", find_single_number(input_numbers))





