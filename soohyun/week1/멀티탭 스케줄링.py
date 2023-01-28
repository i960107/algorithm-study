from typing import List, Set, Dict, Deque
from collections import defaultdict, deque


def solution(n: int, k: int, usage: List[int]) -> int:
    # 남은 사용횟수가 적더라도, 곧 사용된다면, 제거하면 안되는데..
    device_usage = defaultdict(deque)

    for index, device in enumerate(usage):
        device_usage[device].append(index)

    power_bar = set()
    removed = 0

    for index, device in enumerate(usage):
        device_usage[device].popleft()

        if device in power_bar:
            continue

        if len(power_bar) < n:
            power_bar.add(device)
            continue

        least_utilized = get_least_utilized_device_in_near_future(device_usage, power_bar)
        power_bar.remove(least_utilized)
        power_bar.add(device)
        removed += 1

    return removed


# 사용되기까지 시간이 가장 긴 전자제품 찾기:
def get_least_utilized_device_in_near_future(device_usage: Dict[int, Deque], power_bar: Set[int]) -> int:
    least_utilized_device = None
    for device in power_bar:
        if not device_usage[device]:
            return device
        # 주의!
        if not least_utilized_device or device_usage[least_utilized_device] < device_usage[device]:
            least_utilized_device = device
    return least_utilized_device


n, k = map(int, input().split())
usage = list(map(int, input().split()))
print(solution(n, k, usage))
