def is_valid(parentheses):
    stack = []

    matching_parentheses = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for p in parentheses:
        if p == "(" or p == "{" or p == "[":
            stack.append(p)
        elif stack == [] or stack.pop() != matching_parentheses[p]:
            return False

    return stack == []


print(is_valid("((()))"))
print(is_valid("[()]{}"))
print(is_valid("({[)]"))
print(is_valid("()(){(())"))
print(is_valid(""))
print(is_valid("([{}])()"))
