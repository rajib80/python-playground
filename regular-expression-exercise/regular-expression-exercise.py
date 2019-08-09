import re

file_handler = open("regex_sum_271728.txt")

total = 0

for line in file_handler:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            total += int(number)

print(total)
