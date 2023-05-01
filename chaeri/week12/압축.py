def solution(msg):
    answer = []

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = dict(zip(alphabet, range(1, 27)))
    print(dic)

    w, c = 0, 0
    while True:
        c += 1	
        if c == len(msg):	
            answer.append((dic[msg[w:c]]))
            break
        
        # 사전에 없을 때
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1 
            answer.append(dic[msg[w:c]])
            w = c	

    return answer