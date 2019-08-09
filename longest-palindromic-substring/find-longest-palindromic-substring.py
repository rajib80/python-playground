def add_delimeter(string, character):
    string_with_delimeter = "@" + character + \
                            character.join(list(string.lower())) + character + "$"
    return string_with_delimeter, len(string_with_delimeter)


def find_palindromic_substring(input_string, delimeter):
    if input_string == '':
        return [0]

    text, text_length = add_delimeter(input_string, delimeter)
    palindromic_substring_length = [0] * text_length

    center = 1
    right = 1
    index = 1

    while index < len(text) - 1:
        mirror = 2 * center - index

        if index < right:
            palindromic_substring_length[index] = min(right - index,
                                                      palindromic_substring_length[mirror])

        while text[index + (1 + palindromic_substring_length[index])] == \
                text[index - (1 + palindromic_substring_length[index])]:
            palindromic_substring_length[index] += 1

        if index + palindromic_substring_length[index] > right:
            center = index
            right = index + palindromic_substring_length[index]

        index += 1

    return palindromic_substring_length


def longest_palindromic_substring(string, delimeter='|'):
    palindromic_substring_length = find_palindromic_substring(string, delimeter)
    print(palindromic_substring_length)
    longest = max(palindromic_substring_length)
    print("Longest length =", longest)

    print("Longest length index = ", palindromic_substring_length.index(longest))

    if longest % 2 != 0:
        ctr_ind = int(palindromic_substring_length.index(longest) / 2) - 1
    else:
        ctr_ind = int(palindromic_substring_length.index(longest) / 2)

    print("Center index = ", ctr_ind)
    half_word = int(longest / 2)

    start_index, end_index = ctr_ind - half_word, ctr_ind + half_word
    end_index += 0 if longest % 2 == 0 else 1

    print(f"Start index = {start_index} End index = {end_index}")

    return start_index, end_index


test_string = "babcbabcbaccba"
start, end = longest_palindromic_substring(test_string)
palindromic_substring = test_string[start:end]
print(f"palindromic_substring = {palindromic_substring}")


test_string = "banana"
start, end = longest_palindromic_substring(test_string)
palindromic_substring = test_string[start:end]
print(f"palindromic_substring = {palindromic_substring}")


test_string = "million"
start, end = longest_palindromic_substring(test_string)
palindromic_substring = test_string[start:end]
print(f"palindromic_substring = {palindromic_substring}")


