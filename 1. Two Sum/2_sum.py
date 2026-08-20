from typing import List

"""
my implementation adds each value of num to a hashmap,
we calculate the difference of the target of the current value,
and check if that exists in the hashmap before we add our value.
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            return [hash_table[target - nums[i]], i]
        hash_table[nums[i]] = i
    return []


tests = [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]]
]

for idx, test in enumerate(tests):
    if twoSum(test[0], test[1]) == test[2]:
        print(f"Test {idx} Success")