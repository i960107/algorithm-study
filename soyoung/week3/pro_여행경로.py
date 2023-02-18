def solution(tickets):
    dic = {}
    # dic 정보를 담는 과정
    for a, b in tickets:
        if a not in dic.keys():
            dic[a] = [b]
        if a in dic.keys() and b not in dic[a]:
            dic[a].append(b)
    for i in dic.keys():
        dic[i].sort(reverse=True)
    print(dic)
    path = []
    stack = ["ICN"]
    while stack:
        city = stack[-1]
        # city가 dic에 없거나 dic[city]가 없는경우, path에 저장
        if city not in dic or not dic[city]:
            path.append(stack.pop())
        # city를 다시 스택에 넣고, city의 도착점 중 가장 마지막 지점을 꺼내와서 스택에 저장
        else:
            stack.append(dic[city].pop())
    return path[::-1]




