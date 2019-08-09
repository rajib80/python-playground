# You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.

numbers = [4, 7, 1, -3, 2]
target = 5
print(f"Input numbers: {numbers}")
print(f"Target = {target}")

# Two-pass Hash Table
two_pass_hash_table = {}

for index in range(len(numbers)):
    two_pass_hash_table[numbers[index]] = index

for index in range(len(numbers)):
    if target - numbers[index] in two_pass_hash_table:
        if two_pass_hash_table[target - numbers[index]] != index:
            print("The target is a sum of the following two numbers:")
            print(numbers[index], numbers[two_pass_hash_table[target - numbers[index]]])
            break


# One-pass Hash Table
one_pass_hash_table = {}

for index, number in enumerate(numbers):
    if target - number in one_pass_hash_table:
        print("The target is a sum of the following two numbers:")
        print(numbers[one_pass_hash_table[target - number]], numbers[index])
        break
    one_pass_hash_table[number] = index
