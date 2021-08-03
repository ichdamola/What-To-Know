def valid_parenthesis(s):
    stack = []
    lookup = {")":"(", "]":"[", "}":"{"}

    for c in s:
        if c in lookup.values():
            stack.append(c)
        elif stack and lookup[c] == stack[-1]:
            stack.pop()
        else:
            return False
    
    return stack == []

print(valid_parenthesis("()"))
print(valid_parenthesis("()[]{}"))
print(valid_parenthesis("(]"))
print(valid_parenthesis("([)]"))