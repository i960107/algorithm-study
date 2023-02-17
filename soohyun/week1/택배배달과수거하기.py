from typing import List


def solution(cap: int, n: int, deliveries: List[int], pickups: List[int]) -> int:
    total_distance = 0
    previous_last = n - 1

    while True:
        # 방문해야하는 가장 먼 거리의 집
        last = get_last_home_to_visit(previous_last, deliveries, pickups)
        if last == 0:
            break
        previous_last = last
        total_distance += ((last + 1) * 2)

        deliver_and_pickup(cap, last, deliveries, pickups)
    return total_distance


def get_last_home_to_visit(previous_last: int, deliveries: List[int], pickups: List[int]) -> int:
    for home in range(previous_last, 0, -1):
        if deliveries[home] + pickups[home] != 0:
            return home
    return 0


def deliver_and_pickup(cap: int, last_home: int, deliveries: List[int], pickups: List[int]):
    home = last_home
    delivered = 0
    pickuped = 0

    while home > 0:

        delivery = min(deliveries[home], cap - delivered)
        delivered += delivery
        deliveries[home] -= delivery

        pickup = min(pickups[home], cap - pickuped)
        pickuped += pickup
        pickups[home] -= pickup

        home -= 1

        if delivered == cap and pickuped == cap:
            break


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
