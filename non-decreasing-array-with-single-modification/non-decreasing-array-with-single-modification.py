# You are given an array of integers in an arbitrary order. 
# Return whether or not it is possible to make the array non-decreasing 
# by modifying at most 1 element to any value.
# We define an array is non-decreasing if array[i] <= array[i + 1] 
# holds for every i (1 <= i < n).

def check(numbers):
    count = 0
    length = len(numbers)
    index = 0

    while index < length - 1 and count <= 1:
        if numbers[index] > numbers[index + 1]:
            if index > 0:
                if numbers[index - 1] <= numbers[index + 1]:
                    numbers[index] = numbers[index - 1]
                else:
                    numbers[index + 1] = numbers[index]
            count += 1
        index += 1

    return count <= 1


print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False

