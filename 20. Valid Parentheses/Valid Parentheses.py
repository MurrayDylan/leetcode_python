def isValid(s: str) -> bool:
    stack = []
    brackets = {
        "}": "{",
        ")": "(",
        "]": "[",
        ">": "<"
    }

    for c in s:
        if c in brackets.values() :
            stack.append(c)
        elif c in brackets:
            if not stack:
                return False
            stack_top = stack.pop()
            if brackets.get(c) is not stack_top :
                return False
    if not stack:
        return True
    return False


def test() :
    tests = [
        [
            "()",
            True
        ],
        [
            "({+})",
            True
        ],
        [
            "(]",
            False
        ],
        [
            "([)]",
            False
        ],
        [
            "[",
            False
        ]
    ]
    for test in tests:
        ret = isValid(test[0])
        if ret == test[1] :
            print("-- TEST PASS --")
            print(f"S = {test[0]}")
            print(f"Return = {ret}")
        else:
            print("-- TEST FAIL --")
            print(f"S = {test[0]}")
            print(f"Return = {ret}")
test()