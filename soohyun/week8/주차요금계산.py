from typing import List
from collections import defaultdict


def solution(fares: List[int], records: List[str]) -> List[int]:
    history = dict()
    acc_parking_time = defaultdict(int)

    # 누적 시간 계산하기
    for record in records:
        time, car, movement = record.split()
        hh, mm = map(int, time.split(":"))
        # 입차 기록이 있으면
        if movement == "OUT":
            in_hh, in_mm = history[car]
            if in_mm > mm:
                parking_time = (hh - in_hh - 1) * 60 + (mm + 60 - in_mm)
            else:
                parking_time = (hh - in_hh) * 60 + (mm - in_mm)
            acc_parking_time[car] += parking_time
            history.pop(car)
        else:
            history[car] = (hh, mm)

    for car, time in history.items():
        out_hh, out_mm = 23, 59
        in_hh, in_mm = time

        if in_mm > out_mm:
            parking_time = (out_hh - in_hh - 1) * 60 + (out_mm + 60 - in_mm)
        else:
            parking_time = (out_hh - in_hh) * 60 + (out_mm - in_mm)
        acc_parking_time[car] += parking_time

    # 주차 요금 계산하기
    answer = []
    for car, acc_time in sorted(acc_parking_time.items()):
        fee = fares[1]
        if acc_time > fares[0]:
            fee += ((acc_time - fares[0] + fares[2] - 1) // fares[2]) * fares[3]
        answer.append(fee)
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
