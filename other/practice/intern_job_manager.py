"""
You have two interns, Intern A and Intern B, and an array of n tasks.
 For each task i, completing it gives a reward of rewardA[i] if assigned to Intern A,
 and rewardB[i] if assigned to Intern B.
Intern A must complete exactly k tasks, and Intern B will complete the remaining n−k tasks.
Write a function to allocate the tasks in a way that maximizes the total combined reward points.

Input:
rewardA: Array of integers
rewardB: Array of integers
k: Integer (number of tasks Intern A must do)

Output:
Integer representing the maximum total reward.
"""

"""
InternA     InternB
   1           2
   4           6
   8           3
   2           2
   5           2

"""


def solution(rewardA: list[int], rewardB: list[int], k: int) -> int :
    differences = [a-b for a, b in zip(rewardA, rewardB)]

    differences.sort(reverse=True)

    baseline = sum(rewardB)

    best = baseline + sum(differences[:k])

    return best


def test_solution():
    tests = [
        [
            [80, 40, 90, 20, 70, 50],
            [30, 70, 50, 60, 20, 40],
            4,
            420,
        ],
        [
            [1, 4, 8, 2, 5],
            [2, 6, 3, 2, 2],
            3,
            23,
        ]
    ]

    for test in tests:
        res = solution(test[0], test[1], test[2])
        if res == test[3] :
            print(f"Success! returned {res}")
        else:
            print(f"Failure! returned {res}")


test_solution()