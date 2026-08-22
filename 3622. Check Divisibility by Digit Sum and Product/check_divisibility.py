"""
You are given a positive integer n.
Determine whether n is divisible by the sum of the following two values:
The digit sum of n (the sum of its digits).
The digit product of n (the product of its digits).
Return true if n is divisible by this sum; otherwise, return false.
"""

def checkDivisibility(n: int) -> bool:
    n_list = list(map(int, str(n)))
    digit_sum = 0
    digit_product = 1
    for number in n_list:
        digit_sum += + number
        digit_product *= number
    sum_product_sum = digit_sum + digit_product
    return (sum_product_sum != 0) and (n % sum_product_sum == 0)


def test_checkDivisibility():
    tests = {
        (99, True),
        (23, False),
    }

    for idx, test in enumerate(tests) :
        print(f"Test Passed for test {idx}" if checkDivisibility(test[0]) == test[1] else f"Test Failed for test {idx}")


test_checkDivisibility()