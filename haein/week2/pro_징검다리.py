def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance

    rocks.sort()

    while start <= end:
        # 기준이 되는 최소값
        mid = (start + end) // 2
        # 제거한 돌
        cnt = 0
        # 시작지점
        previous_rock = 0

        for rock in rocks:
            # 더 작은 값 있으면 제거
            if rock-previous_rock < mid:
                cnt += 1
            else:
                # mid 이상이면 괜찮음 (최소값보다 큰 것)
                # 해당 돌부터 또 그 다음 돌들 차가 최소값보다 큰지 봐야
                previous_rock = rock
            # 삭제하려고 한 돌보다 더 많이 삭제되면
            if cnt > n:
                break
        # 너무 많이 삭제되었으면 최솟값보다 작은 게 많은 것
        # 따라서 mid가 작아져야
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer
