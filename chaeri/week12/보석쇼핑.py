def solution(gems):
    answer = [] 
    short = len(gems)+1 
    start, end = 0, 0
    check = len(set(gems)) # 보석의 총 종류 수
    contained = {} 

    while end < len(gems): 

        if gems[end] not in contained: #보석 발견
            contained[gems[end]] = 1 
        else:
            contained[gems[end]] += 1 
            
        end += 1

        if len(contained) == check: #현재 구간내 모든 종류가 다 있다면
            while start < end: 
                if contained[gems[start]] > 1: # start에 해당하는 보석이 구간 내에 하나 이상 있을 때
                    contained[gems[start]] -= 1 
                    start += 1 
                    
                elif short > end - start :
                    short = end - start
                    answer = [start+1, end] # answer와 최단거리 갱신
                    break
                    
                else:
                    break

    return answer