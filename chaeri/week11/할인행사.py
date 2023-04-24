def solution(want, number, discount):
    answer = 0
    wish = {} # 내가 갖고 싶은 거
    cur = {} # 10일 전부터 오늘까지 가질 수 있는 물건들
    
    for i in range(len(want)) : 
        wish[want[i]] = number[i]
        cur[want[i]] = 0
        
    for i in range(len(discount)) :     
        before = i - 10
        # 10일 전 상품 삭제
        if discount[before] in want and before >= 0 : 
            if cur[discount[before]] > 0 : 
                cur[discount[before]] -= 1
        
        if discount[i] in want:
            cur[discount[i]] += 1
        canBuy = True
        
        for key in wish.keys() :
            if wish[key] > cur[key] : 
                canBuy = False
                break
        if canBuy : 
            answer += 1
        
    return answer