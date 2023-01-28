from typing import List


def solution(food_time: List[int], k: int) -> int:
    if sum(food_time) <= k:
        return -1

    time = 0
    while True:
        min_left_count = min([food_count for food_count in food_time if food_count != 0])
        left_foods = sum([1 for count in food_time if count > 0])

        if time + min_left_count * left_foods >= k:
            break

        for food, count in enumerate(food_time):
            if count > 0:
                food_time[food] -= min_left_count

        time += min_left_count * left_foods

    food = -1
    while time < k:
        food += 1
        if food_time[food] == 0:
            continue
        time += 1
        food_time[food] -= 1

    return (food + 1) % len(food_time) + 1


print(solution([3, 1, 2], 5))
