def solution_fail(storey):
    if storey < 10:
        return storey if storey <= 5 else 10 - storey + 1
        
    count = 0
    
    storey = str(storey)
    n = len(storey)
    
    higher_than = False
    for index in range(n -1):
        now = storey[index] 
        
        nxt_index = index + 1
        while nxt_index < n - 1 and storey[nxt_index] == "5":
            nxt_index += 1
        nxt = storey[nxt_index]
            
        if higher_than:
            if nxt <= "5":
                count += (10 - int(now))
                higher_than = False
            else:
                count += (10 - int(now) - 1)
        else:
            if nxt <= "5":
                count += (int(now))
            else:
                count += (int(now) + 1) if int(now) < 9 else 1
                higher_than = True
            
    if higher_than:
        count += (10 - int(storey[-1]))
    else:
        count += (int(storey[-1]))
        
    return count


def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        if remainder > 5:
            answer += (10 - remainder)
            storey += (10)
        elif remainder < 5:
            answer += remainder
        else:
            if(storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10
    return answer

