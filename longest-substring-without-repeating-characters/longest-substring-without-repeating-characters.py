def longest_substring_without_repeating_characters(input_string):
    seen = {}
    max_length = 0
    start = 0

    for end in range(len(input_string)):
        print(input_string[end])
        if input_string[end] in seen:
            start = max(start, seen[input_string[end]] + 1)
        print(f"start = {start}")
        seen[input_string[end]] = end
        print(seen)
        max_length = max(max_length, end - start + 1)
        print(f"max length = {max_length}")

    return max_length


print(longest_substring_without_repeating_characters("abrkaabcdefghijjxxx"))

