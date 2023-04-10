def solution(play_time, adv_time, logs):
    def convert_from_time(s: str) -> int:
        result = 0
        for x in s.split(":"):
            result = result * 60 + int(x)
        return result

    converted_play_time = convert_from_time(play_time)
    converted_adv_time = convert_from_time(adv_time)
    prefix = [0] * converted_play_time
    for log in logs:
        start, end = log.split("-")
        converted_start = convert_from_time(start)
        converted_end = convert_from_time(end)
        prefix[converted_start] += 1
        if converted_end < len(prefix):
            prefix[converted_end] -= 1

    for index in range(1, len(prefix)):
        prefix[index] += prefix[index - 1]

    total_adv_time = sum(prefix[:converted_adv_time])

    adv_start_time = 0
    max_adv_time = total_adv_time

    for end in range(converted_adv_time, len(prefix)):
        total_adv_time -= prefix[end - converted_adv_time]
        total_adv_time += prefix[end]
        if total_adv_time > max_adv_time:
            max_adv_time = total_adv_time
            adv_start_time = end - converted_adv_time + 1

    def convert_to_time(num: int) -> str:
        result = []
        for i in range(2, -1, -1):
            # result.append('%02d' % ((num // (60 ** i))))
            # zfill- 0, ljust - 특정 문자지정
            result.append(str(num // (60 ** i)).zfill(0))
            num -= num // (60 ** i) * (60 ** i)

        return ':'.join(result)

    return convert_to_time(adv_start_time)
