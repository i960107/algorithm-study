N = int(input())
rooms = list(map(int, input().split()))

B, C = map(int, input().split())

answer = 0
for students in rooms:
    # 주 감독관은 무조건 한명 있어야 함!
    # + C - 1 => math.ceil의 효과
    teachers = 1 + ((students - B if students > B else 0) + C - 1) // C
    # if (students + C) // C < teachers:
    #     teachers = (students + C) // C
    answer += teachers
print(answer)
