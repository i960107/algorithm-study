def solution(id_list, report, k):
    answer = []
    result = {}
    fbd_user = []

    for id in id_list:
        result[id] = [[], 0, 0]
    
    for case in set(report):
        result[case.split()[0]][0].append(case.split()[1])
        result[case.split()[1]][1] += 1    

    for user in id_list:
        if result[user][1] >= k:
            fbd_user.append(user)

    for user in id_list:
        for forbidden in fbd_user:
            if forbidden in result[user][0]:
                result[user][2] += 1
        answer.append(result[user][2])

    return answer