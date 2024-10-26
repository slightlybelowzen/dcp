def is_valid(inp: str) -> bool:
    stack = []
    map = {')': '(', '}': '{', ']': '['}
    for s in inp:
        if s in map:
            top = stack.pop if stack else '$'
            if top != map[s]:
                return False
        else:
            stack.append(s)
    return not(stack)

if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("((()))") == True
    assert is_valid("(([))") == False
