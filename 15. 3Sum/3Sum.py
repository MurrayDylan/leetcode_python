"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]],
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def twoSum(nums, target):
    hash_table = {}
    for i in range(len(nums)) :
        if target - nums[i] in hash_table :
            return [hash_table[target - nums[i]], i]
        hash_table[nums[i]] = i
    return []

def threeSum(nums: list[int], target=0) -> list[list[int]]:
    nums.sort()
    results = []

    for i in range(len(nums) - 2) :
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1] :
                    left = left + 1

                while left < right and nums[right] == nums[right - 1]:
                    right = right - 1

                left = left + 1
                right = right - 1

            elif current_sum < target:
                left = left + 1

            else:
                right = right - 1


    return results

def test_threeSum():
    tests = [
        ([-1, 0, 1, 2, -1, -4], 0, ([-1, -1, 2], [-1, 0, 1])),
        ([0, 0, 1], 0, ()),
        ([0, 0, 0], 0, ([0, 0, 0],)),
        ([0, 0, 0, 0], 0, ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]))
    ]

    for test_num, (nums, target, expected_triplets) in enumerate(tests, start=1):
        actual_result = threeSum(nums, target)

        if actual_result == list(expected_triplets):
            print(f"Test {test_num}: Passed")
        else:
            print(f"Test {test_num}: Failed (Got {actual_result}, expected {list(expected_triplets)})")


test_threeSum()