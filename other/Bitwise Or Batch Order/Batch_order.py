import math

def solution(batchOrders : list[int] ) -> int:
    """
    batchOrders : [1, 3, 5]
    bitwise or of any values cannot be contained in original list
    return no. of times is contained
    """

    batch_length = len(batchOrders)
    count = 0

    for i in range(batch_length):
        bit_val = 0
        bit_val = bit_val | batchOrders[i]
        if bit_val in batchOrders:
            count += 1
        for j in range(i+1, batch_length, 1):
            bit_val = bit_val | batchOrders[j]
            if bit_val in batchOrders:
                count += 1

    print(count)
    return count

    print(all_orders)


def test():
    tests = [
        [
            [1, 3, 7],
            6
        ]
    ]
    for test in tests :
        ret = solution(test[0])
        if ret == test[1] :
            print("PASS")
        else :
            print("FAIL")

test()