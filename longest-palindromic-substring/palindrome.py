def add_delimeter(string, character):
    string_with_delimeter = character + character.join(list(string.lower())) + character
    print(string_with_delimeter, len(string_with_delimeter))
    return string_with_delimeter, len(string_with_delimeter)


def reset_position(left, center, right, adj_right):
    print("Calling reset_position.........")
    print(f"Left = {left}, Center = {center}, Right = {right}, Adjusted Right = {adj_right}")
    if (left + right) / 2 == center:
        center = adj_right
    left = center - (right - center)
    print("Returning reset_position.........")
    print(f"Left = {left}, Center = {center}, Right = {right}, Adjusted Right = {adj_right}")
    return left, center, right


def is_symmetric(left, left_edge, right, right_edge, text):
    return (left >= left_edge and
            right <= right_edge and
            text[left] == text[right])


def expand_linear(center, right, adjusted_right, palindromic_substring_length):
    print("Calling expand_linear..................")
    print(f"Center = {center}, Right = {right}, Adjusted Right = {adjusted_right}")

    for i in range(1, right - center):
        distance_to_edge = adjusted_right - (center + i)

        if palindromic_substring_length[center - i] < distance_to_edge:
            palindromic_substring_length[center + i] = palindromic_substring_length[center - i]
        elif palindromic_substring_length[center - i] > distance_to_edge:
            palindromic_substring_length[center + i] = distance_to_edge
        else:
            palindromic_substring_length[center + i] = distance_to_edge
            center += i
            break

    print("Returning expand_linear..................")
    print(f"Center = {center}, Right = {right}, Adjusted Right = {adjusted_right}")

    return center, palindromic_substring_length


def find_palindromic_substring(input_string, delimeter):
    if input_string == '':
        return [0]

    text, text_length = add_delimeter(input_string, delimeter)
    palindromic_substring_length = [0] * text_length

    left, center, right = 1, 1, 1
    left_edge, right_edge = 1, len(text) - 2

    print("At start right_edge = ", right_edge)

    iteration = 1

    while right <= right_edge:
        print("Iteration : ", iteration, "  ##########################################")
        print(f"Left = {left}, Left_Edge = {left_edge}, Right = {right}, Right_Edge = {right_edge}")
        # expand naively around current center; single char is palindrome
        while is_symmetric(left, left_edge, right, right_edge, text):
            print("text[right] = ", text[right])
            if text[right] != delimeter:
                palindromic_substring_length[center] += 1 if left == right else 2
                print("center = ", center, "palindromic_substring_length[center] = ", palindromic_substring_length[center])
            left, right = left - 1, right + 1

        # find adjusted right index that always falls on a delimeter

        if palindromic_substring_length[center] > 0 and left > 0:
            adjusted_right = right - 1
        else:
            adjusted_right = right

        center, palindromic_substring_length = expand_linear(center, right, adjusted_right, palindromic_substring_length)
        left, center, right = reset_position(left, center, right, adjusted_right)

        print("End of iteration : ", iteration, "  ##########################################")
        iteration += 1

    return palindromic_substring_length


def longest_palindromic_substring(string, delimeter='|'):
    palindromic_substring_length = find_palindromic_substring(string, delimeter)
    print(palindromic_substring_length)
    longest = max(palindromic_substring_length)
    print(longest)

    ctr_ind = int(palindromic_substring_length.index(longest) / 2)
    half_word = int(longest / 2)

    start_index, end_index = ctr_ind - half_word, ctr_ind + half_word
    end_index += 0 if longest % 2 == 0 else 1

    return start_index, end_index


test_string = "babcbabcbaccba"
# test_string = "banana"
start, end = longest_palindromic_substring(test_string)
palindromic_substring = test_string[start:end]
print(palindromic_substring)

