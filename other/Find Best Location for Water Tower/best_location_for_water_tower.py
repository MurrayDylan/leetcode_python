"""
Given an m × n grid of positive integers representing heights,
and two coordinates representing villages,

find a location for a water tower such that water can flow to both villages.

Water can only flow from a higher/equal point to a lower/equal point.
If multiple locations work, return the one with the highest altitude.
"""

def solution(map: list[list[int]], t1: tuple[int, int], t2: tuple[int, int]):
    for row in map:
        print(f"{row}")
    print("")

    t1_access_set = build_access_table(map, t1)
    t2_access_set = build_access_table(map, t2)

    print(f"Town 1: {t1_access_set}")
    print(f"Town 2: {t2_access_set}")

    overlap = t1_access_set & t2_access_set
    print(f"{overlap}")

    if not overlap:
        return None

    best_coord, best_height = max(overlap, key=lambda item: item[1])

    print(f"Best place for the tower is {best_coord}, with a height of {best_height}")

    return best_coord

def build_access_table(map: list[list[int]], start: tuple[int, int], visited: set[tuple[int, int], int]=None) -> set[tuple[int, int], int]:
    if visited is None :
        visited = set()

    x, y = start
    current_height = map[y][x]

    visited.add(((x, y), current_height))

    # left
    if (x-1 >= 0) and (map[y][x-1] >= current_height) and (x-1, y) not in visited:
        build_access_table(map, (x-1, y), visited)

    # up
    if (y+1 < len(map)) and (map[y+1][x] >= current_height) and (x, y+1) not in visited :
        build_access_table(map, (x, y+1), visited)

    # right
    if (x+1 < len(map[0])) and (map[y][x+1] >= current_height) and (x+1, y) not in visited :
        build_access_table(map, (x+1, y), visited)

    # down
    if (y-1 >= 0) and (map[y-1][x] >= current_height) and (x, y-1) not in visited :
        build_access_table(map, (x, y-1), visited)
    return visited

def test_solution():
    tests = [
        [
            [
                [1, 2, 3, 4],
                [2, 3, 6, 5],
                [3, 4, 7, 2],
                [4, 5, 6, 1]
            ],
            (3, 1),
            (3, 3)
        ]
    ]

    for test in tests:
        solution(test[0], test[1], test[2])

test_solution()